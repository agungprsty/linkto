<template>
  <div class="bg-brand-bg text-black antialiased min-h-screen flex flex-col selection:bg-brand-pink selection:text-white">
    <!-- Minimal Nav -->
    <nav class="w-full bg-brand-bg border-b-4 border-black">
      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16 items-center">
          <NuxtLink to="/" class="flex items-center gap-2">
            <div class="w-8 h-8 bg-black rounded-full flex items-center justify-center -rotate-12 hover:rotate-0 transition-transform">
              <Icon name="ph:link" class="text-brand-yellow text-xl font-bold" />
            </div>
            <span class="font-black text-2xl tracking-tight">Linkto.</span>
          </NuxtLink>
          <p class="text-sm font-bold text-gray-500 hidden sm:block">
            Already have an account? <NuxtLink to="/auth/login" class="text-brand-blue underline decoration-4 underline-offset-2 hover:text-black transition-colors">Log in</NuxtLink>
          </p>
        </div>
      </div>
    </nav>

    <!-- Register Form -->
    <main class="flex-1 flex items-center justify-center px-4 py-12 relative">
      <!-- Background decorations (pointer-events-none to prevent blocking clicks) -->
      <div class="absolute top-20 right-10 w-40 h-40 bg-brand-green border-4 border-black rounded-full -z-10 float-slow pointer-events-none" style="animation-delay: 1s;" />
      <div class="absolute bottom-20 left-10 w-32 h-32 bg-brand-yellow border-4 border-black rounded-lg -z-10 float-slow pointer-events-none" style="animation-delay: 3s;" />
      <div class="absolute top-1/3 left-1/4 w-24 h-24 bg-brand-pink border-4 border-black -z-10 -rotate-12 pointer-events-none" />
      <div class="absolute bottom-1/3 right-1/4 w-16 h-16 bg-brand-blue border-4 border-black rounded-full -z-10 pointer-events-none" />

      <div class="w-full max-w-md relative z-10">
        <div class="bg-white border-4 border-black shadow-brutal-lg p-8 sm:p-10">
          <!-- Header -->
          <div class="text-center mb-8">
            <h1 class="text-3xl sm:text-4xl font-black">Create your account</h1>
            <p class="text-base font-semibold text-gray-500 mt-2">Join 10M+ creators on Linkto</p>
          </div>

          <!-- Error message -->
          <div v-if="auth.error" class="bg-red-50 border-4 border-red-500 p-4 mb-6">
            <p class="font-bold text-red-700 text-sm">{{ auth.error || 'An unexpected error occurred' }}</p>
          </div>

          <!-- Form -->
          <form class="space-y-5" @submit.prevent="handleRegister">
            <div>
              <label for="email" class="block font-bold text-sm mb-2">Email address</label>
              <input id="email" v-model="email" type="email" placeholder="you@example.com" required autocomplete="email"
                class="w-full border-4 border-black py-3.5 px-4 font-semibold text-base bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
            </div>

            <div>
              <label for="password" class="block font-bold text-sm mb-2">Password</label>
              <input id="password" v-model="password" type="password" placeholder="Create a strong password" required autocomplete="new-password"
                class="w-full border-4 border-black py-3.5 px-4 font-semibold text-base bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
              <!-- Password strength -->
              <div class="flex gap-2 mt-3">
                <div v-for="i in 3" :key="i" class="h-2 flex-1 rounded-full" :class="passwordStrengthClass(i)"></div>
              </div>
              <p class="text-xs font-semibold text-gray-400 mt-2">Use at least 8 characters, one uppercase, one number & one symbol</p>
            </div>

            <div class="flex items-start gap-3 text-sm">
              <input type="checkbox" required class="w-5 h-5 mt-0.5 border-4 border-black accent-black flex-shrink-0">
              <span class="font-semibold text-gray-600">I agree to the <NuxtLink to="/terms" class="text-brand-blue font-bold underline decoration-2 underline-offset-2">Terms of Service</NuxtLink> and <NuxtLink to="/privacy" class="text-brand-blue font-bold underline decoration-2 underline-offset-2">Privacy Policy</NuxtLink>.</span>
            </div>

            <button type="submit" :disabled="auth.loading ? true : false"
              class="w-full bg-brand-pink text-black font-black text-lg py-4 border-4 border-black shadow-brutal hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed">
              <template v-if="auth.loading">
                <Icon name="ph:spinner" class="animate-spin" /> Creating account...
              </template>
              <template v-else>
                Create Account <Icon name="ph:arrow-right" class="font-bold" />
              </template>
            </button>
          </form>

          <!-- Divider -->
          <div class="flex items-center gap-4 mb-6 mt-8">
            <div class="flex-1 h-1 bg-black" />
            <span class="text-sm font-bold text-gray-500">OR</span>
            <div class="flex-1 h-1 bg-black" />
          </div>

          <!-- Social -->
          <div class="space-y-3 mb-6">
            <button @click="googleLogin" type="button"
              class="w-full flex items-center justify-center gap-3 bg-white border-4 border-black shadow-brutal-sm py-3.5 font-bold text-base hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
              <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none">
                <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z" fill="#4285F4"/>
                <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
                <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
              </svg>
              Sign up with Google
            </button>

            <button @click="appleLogin" type="button"
              class="w-full flex items-center justify-center gap-3 bg-white border-4 border-black shadow-brutal-sm py-3.5 font-bold text-base hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
              <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
              </svg>
              Sign up with Apple
            </button>
          </div>
        </div>

        <p class="text-center mt-6 font-semibold text-gray-500">
          Already have an account? <NuxtLink to="/auth/login" class="text-brand-blue font-black underline decoration-4 underline-offset-2 hover:text-black transition-colors">Log in</NuxtLink>
        </p>
      </div>
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default',
})

import { useAuthStore } from '~/stores/auth'

const auth = useAuth()
const email = ref('')
const password = ref('')

// Reset error & loading state when mounting this page
onMounted(() => {
  const store = useAuthStore()
  store.error = null
  store.loading = false
})

function getPasswordStrength(): number {
  const val = password.value
  let strength = 0
  if (val.length >= 8) strength++
  if (/[A-Z]/.test(val) && /[a-z]/.test(val)) strength++
  if (/[0-9]/.test(val) && /[^A-Za-z0-9]/.test(val)) strength++
  return strength
}

function passwordStrengthClass(barIndex: number): string {
  const strength = getPasswordStrength()
  if (barIndex <= strength) {
    if (strength === 1) return 'bg-red-500'
    if (strength === 2) return 'bg-yellow-500'
    return 'bg-green-500'
  }
  return 'bg-gray-200'
}

async function handleRegister() {
  // Validate inputs before calling API
  if (!email.value || !password.value) {
    const store = useAuthStore()
    store.error = 'Please fill in all fields'
    return
  }
  try {
    await auth.register(email.value, password.value)
  } catch {
    // Error handled by store
  }
}

function googleLogin() {
  const config = useRuntimeConfig()
  window.location.href = `${config.public.apiBaseUrl}/auth/google/login`
}

function appleLogin() {
  const config = useRuntimeConfig()
  window.location.href = `${config.public.apiBaseUrl}/auth/apple/login`
}

useSeoMeta({
  title: 'Sign Up — Linkto',
})
</script>
