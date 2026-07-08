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
  async function login(email: string, password: string): Promise<boolean> {
    const success = await authStore.login(email, password)
    return success && !authStore.error
  }

  async function register(email: string, password: string, fullName?: string, usernameVal?: string): Promise<boolean> {
    const success = await authStore.register(email, password, fullName, usernameVal)
    return success && !authStore.error
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
