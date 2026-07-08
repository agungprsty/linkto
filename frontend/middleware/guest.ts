import { useAuthStore } from '~/stores/auth'

export default defineNuxtRouteMiddleware(async (to, from) => {
  // Only protect auth pages (login, register)
  if (!to.path.startsWith('/auth')) return

  // Cek session cookie (works on both server and client via useCookie)
  const session = useCookie('linkto_session')

  // Tidak ada session cookie → user pasti belum login → tampilkan auth page
  if (!session.value) return

  // ── Server-side ──
  // Session cookie ada → jangan render HTML auth page,
  // langsung redirect biar SSR kirim halaman dashboard.
  // Nanti dashboard middleware/auth.ts yang handle refresh token.
  if (process.server) {
    return navigateTo('/dashboard')
  }

  // ── Client-side ──
  // Session cookie ada, coba restore auth state dari refresh token
  const authStore = useAuthStore()

  if (!authStore.isAuthenticated) {
    await authStore.initAuth()
  }

  if (authStore.isAuthenticated) {
    return navigateTo('/dashboard')
  }

  // Token refresh gagal — session cookie stale, hapus
  session.value = null
})
