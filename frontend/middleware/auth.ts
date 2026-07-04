export default defineNuxtRouteMiddleware(async (to, from) => {
  // Only protect dashboard routes
  if (!to.path.startsWith('/dashboard')) return

  // Only run on client-side
  if (process.server) return

  const authStore = useAuthStore()

  // Try to initialize auth if not already done
  if (!authStore.isAuthenticated) {
    await authStore.initAuth()
  }

  // If still not authenticated, redirect to login
  if (!authStore.isAuthenticated) {
    return navigateTo('/auth/login', { redirectCode: 302 })
  }
})
