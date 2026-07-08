import { defineNuxtPlugin } from '#app'
import { useAuthStore } from '~/stores/auth'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()
  const baseUrl = config.public.apiBaseUrl

  // Guard to prevent concurrent refresh attempts
  let isRefreshing = false

  const api = $fetch.create({
    baseURL: baseUrl,
    credentials: 'include', // Send cookies (refresh_token)
    headers: {
      'Content-Type': 'application/json',
    },
    onRequest({ options }) {
      // Try to add access token from store
      const authStore = useAuthStore()
      if (authStore.accessToken) {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        ;(options.headers as any)['Authorization'] = `Bearer ${authStore.accessToken}`
      }
    },
    async onResponseError({ response, request }) {
      // Only handle 401 errors
      if (response.status !== 401) return

      // Skip auth endpoints to prevent recursive refresh loops
      const requestUrl = typeof request === 'string' ? request : ''
      if (requestUrl.includes('/auth/')) return

      // Prevent concurrent refresh attempts
      if (isRefreshing) return
      isRefreshing = true

      try {
        const authStore = useAuthStore()
        const refreshed = await authStore.refreshToken()
        if (refreshed) {
          await authStore.fetchUser()
        } else {
          await authStore.logout()
          // Redirect to login if on dashboard page
          const router = useRouter()
          if (router?.currentRoute.value.path.startsWith('/dashboard')) {
            router.push('/auth/login')
          }
        }
      } finally {
        isRefreshing = false
      }
    },
  })

  // Provide $api to the app
  nuxtApp.provide('api', api)
})

// Extend NuxtApp type
declare module '#app' {
  interface NuxtApp {
    $api: typeof $fetch
  }
}
