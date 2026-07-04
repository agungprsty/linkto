import { useAuthStore } from '~/stores/auth'

export function useAuth() {
  const authStore = useAuthStore()
  const router = useRouter()
  const route = useRoute()

  // Computed
  const isAuthenticated = computed(() => authStore.isAuthenticated)
  const user = computed(() => authStore.user)
  const loading = computed(() => authStore.loading)
  const error = computed(() => authStore.error)
  const username = computed(() => authStore.username)

  // Methods
  async function login(email: string, password: string) {
    await authStore.login(email, password)
    if (authStore.isAuthenticated) {
      await router.push('/dashboard')
    }
  }

  async function register(email: string, password: string, fullName?: string, usernameVal?: string) {
    await authStore.register(email, password, fullName, usernameVal)
    if (authStore.isAuthenticated) {
      await router.push('/dashboard')
    }
  }

  async function logout() {
    await authStore.logout()
    await router.push('/')
  }

  async function initAuth() {
    await authStore.initAuth()
  }

  return {
    isAuthenticated,
    user,
    loading,
    error,
    username,
    login,
    register,
    logout,
    initAuth,
  }
}
