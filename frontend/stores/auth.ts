import { defineStore } from 'pinia'
import type { User, AuthResponse } from '~/types'

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
    }
  }

  async function refreshToken(): Promise<boolean> {
    try {
      const { $api } = useNuxtApp()
      const data = await $api('/auth/refresh', { method: 'POST' }) as AuthResponse
      accessToken.value = data.access_token
      return true
    } catch {
      accessToken.value = null
      user.value = null
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
      // Token might be expired
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
    // Check if we have a token from cookies
    // Try to refresh if we have a cookie-based refresh token
    const refreshed = await refreshToken()
    if (refreshed) {
      await fetchUser()
    }
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
