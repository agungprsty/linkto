import { defineStore } from 'pinia'
import type { User, AuthResponse } from '~/types'

// ── Generic cookie helpers ──
function setCookie(name: string, value: string, days: number): void {
  if (import.meta.server) return
  const date = new Date()
  date.setDate(date.getDate() + days)
  document.cookie = `${name}=${encodeURIComponent(value)}; path=/; expires=${date.toUTCString()}; SameSite=Lax; Secure`
}

function getCookie(name: string): string | null {
  if (import.meta.server) return null
  const match = document.cookie.match(new RegExp(`(?:^|;\\s*)${name}=([^;]*)`))
  return match ? decodeURIComponent(match[1]) : null
}

function removeCookie(name: string): void {
  if (import.meta.server) return
  document.cookie = `${name}=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax; Secure`
}

// ── Session marker cookie (non-sensitive; tracks active login) ──
const SESSION_COOKIE = 'linkto_session'
const SESSION_DURATION_DAYS = 7

// ── Refresh token cookie (used as fallback for body-based refresh) ──
const REFRESH_TOKEN_COOKIE = 'linkto_refresh'
const REFRESH_DURATION_DAYS = 7

function saveRefreshToken(token: string): void {
  setCookie(REFRESH_TOKEN_COOKIE, token, REFRESH_DURATION_DAYS)
}

function getSavedRefreshToken(): string | null {
  return getCookie(REFRESH_TOKEN_COOKIE)
}

function clearSavedRefreshToken(): void {
  removeCookie(REFRESH_TOKEN_COOKIE)
}

// ── Session marker helpers (re-using generic cookie helpers) ──
function setSessionCookie(): void {
  setCookie(SESSION_COOKIE, '1', SESSION_DURATION_DAYS)
}

function clearSessionCookie(): void {
  removeCookie(SESSION_COOKIE)
}

function hasSessionCookie(): boolean {
  return getCookie(SESSION_COOKIE) !== null
}

export const useAuthStore = defineStore('auth', () => {
  // State
  const user = ref<User | null>(null)
  const accessToken = ref<string | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  // Getters
  const isAuthenticated = computed(() => !!accessToken.value && !!user.value)
  const username = computed(() => user.value?.username || '')

  // Actions
  async function login(email: string, password: string): Promise<boolean> {
    loading.value = true
    error.value = null
    try {
      const { $api } = useNuxtApp()
      const data = await $api('/auth/login', {
        method: 'POST',
        body: { email, password },
      }) as AuthResponse

      accessToken.value = data.access_token
      user.value = data.user || null
      setSessionCookie()
      if (data.refresh_token) {
        saveRefreshToken(data.refresh_token)
      }
      return true
    } catch (e: any) {
      const detail = e?.data?.detail
      if (Array.isArray(detail)) {
        error.value = detail.map((d: any) => d.msg).join(', ')
      } else if (typeof detail === 'string') {
        error.value = detail
      } else if (detail?.message) {
        error.value = detail.message
      } else {
        error.value = e?.message || 'Login failed. Please check your credentials.'
      }
      return false
    } finally {
      loading.value = false
    }
  }

  async function register(email: string, password: string, fullName?: string, username?: string): Promise<boolean> {
    loading.value = true
    error.value = null
    try {
      const { $api } = useNuxtApp()
      const body: Record<string, string> = { email, password }
      if (username) body.username = username
      if (fullName) body.full_name = fullName
      const data = await $api('/auth/register', {
        method: 'POST',
        body,
      }) as AuthResponse

      accessToken.value = data.access_token
      user.value = data.user || null
      setSessionCookie()
      if (data.refresh_token) {
        saveRefreshToken(data.refresh_token)
      }
      return true
    } catch (e: any) {
      const detail = e?.data?.detail
      if (Array.isArray(detail)) {
        error.value = detail.map((d: any) => d.msg).join(', ')
      } else if (typeof detail === 'string') {
        error.value = detail
      } else if (detail?.message) {
        error.value = detail.message
      } else {
        error.value = e?.message || 'Registration failed. Please try again.'
      }
      return false
    } finally {
      loading.value = false
    }
  }

  async function logout(): Promise<void> {
    try {
      const { $api } = useNuxtApp()
      await $api('/auth/logout', { method: 'POST' })
    } catch {
      // Clear local state even if server logout fails
    } finally {
      accessToken.value = null
      user.value = null
      error.value = null
      clearSessionCookie()
      clearSavedRefreshToken()
    }
  }

  async function refreshToken(): Promise<boolean> {
    try {
      const { $api } = useNuxtApp()
      // Send refresh token in body as fallback
      // (also works via httpOnly cookie after backend fix to auth.py)
      const savedRt = getSavedRefreshToken()
      const body = savedRt ? { refresh_token: savedRt } : {}
      const data = await $api('/auth/refresh', {
        method: 'POST',
        body,
      }) as AuthResponse
      accessToken.value = data.access_token
      // Save rotated refresh token if server returns a new one
      if (data.refresh_token) {
        saveRefreshToken(data.refresh_token)
      }
      return true
    } catch {
      accessToken.value = null
      user.value = null
      clearSessionCookie()
      clearSavedRefreshToken()
      return false
    }
  }

  async function fetchUser(): Promise<void> {
    if (!accessToken.value) return
    try {
      const { $api } = useNuxtApp()
      const data = await $api('/auth/me') as User
      user.value = data
    } catch {
      // Token might be expired — try to refresh
      const refreshed = await refreshToken()
      if (refreshed) {
        try {
          const { $api } = useNuxtApp()
          const data = await $api('/auth/me') as User
          user.value = data
        } catch {
          await logout()
        }
      } else {
        await logout()
      }
    }
  }

  async function initAuth(): Promise<void> {
    // Only attempt token refresh if we have a session cookie
    // (avoids unnecessary /auth/refresh calls on first visit)
    if (!hasSessionCookie()) return

    const refreshed = await refreshToken()
    if (refreshed) {
      await fetchUser()
    }
    // if refresh fails, cookie is cleared inside refreshToken()
  }

  function $reset() {
    user.value = null
    accessToken.value = null
    loading.value = false
    error.value = null
  }

  return {
    user,
    accessToken,
    loading,
    error,
    isAuthenticated,
    username,
    login,
    register,
    logout,
    refreshToken,
    fetchUser,
    initAuth,
    $reset,
  }
})
