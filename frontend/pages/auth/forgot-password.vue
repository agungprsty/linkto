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
            Remember your password? <NuxtLink to="/auth/login" class="text-brand-blue underline decoration-4 underline-offset-2 hover:text-black transition-colors">Log in</NuxtLink>
          </p>
        </div>
      </div>
    </nav>

    <main class="flex-1 flex items-center justify-center px-4 py-12 relative">
      <!-- Background decorations (pointer-events-none to prevent blocking clicks) -->
      <div class="absolute top-20 left-10 w-40 h-40 bg-brand-blue border-4 border-black rounded-full -z-10 float-slow pointer-events-none" />
      <div class="absolute bottom-20 right-10 w-32 h-32 bg-brand-yellow border-4 border-black rounded-lg -z-10 float-slow pointer-events-none" style="animation-delay: 2s;" />
      <div class="absolute top-1/3 right-1/4 w-24 h-24 bg-brand-pink border-4 border-black -z-10 rotate-12 pointer-events-none" />
      <div class="absolute bottom-1/3 left-1/4 w-16 h-16 bg-brand-green border-4 border-black rounded-full -z-10 pointer-events-none" />

      <div class="w-full max-w-md relative z-10">
        <div class="bg-white border-4 border-black shadow-brutal-lg p-8 sm:p-10">
          <!-- Header -->
          <div class="text-center mb-8">
            <div class="w-16 h-16 bg-black rounded-full flex items-center justify-center mx-auto mb-5 rotate-6 hover:rotate-0 transition-transform">
              <Icon name="ph:lock" class="text-brand-yellow text-3xl font-bold" />
            </div>
            <h1 class="text-3xl sm:text-4xl font-black">Forgot password?</h1>
            <p class="text-base font-semibold text-gray-500 mt-2">No worries. Enter your email and we'll send you a reset link.</p>
          </div>

          <!-- Form -->
          <form v-if="!sent" class="space-y-5" @submit.prevent="handleSubmit">
            <div>
              <label for="email" class="block font-bold text-sm mb-2">Email address</label>
              <input id="email" v-model="email" type="email" placeholder="you@example.com" required
                class="w-full border-4 border-black py-3.5 px-4 font-semibold text-base bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
            </div>

            <button type="submit"
              class="w-full bg-brand-blue text-black font-black text-lg py-4 border-4 border-black shadow-brutal hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full flex items-center justify-center gap-2">
              Send Reset Link <Icon name="ph:paper-plane-right" class="font-bold" />
            </button>
          </form>

          <!-- Sent State -->
          <div v-else class="text-center py-4">
            <div class="w-20 h-20 bg-brand-green border-4 border-black rounded-full flex items-center justify-center mx-auto mb-5 shadow-brutal-sm">
              <Icon name="ph:check" class="text-5xl font-bold text-black" />
            </div>
            <h2 class="text-2xl font-black mb-2">Check your inbox</h2>
            <p class="font-semibold text-gray-500 mb-6">We've sent a password reset link to your email. It should arrive in a few minutes.</p>
            <div class="bg-brand-bg border-4 border-black p-4 mb-6 font-bold text-sm">
              <p class="text-gray-600">Didn't receive the email? Check your spam folder or</p>
              <button @click="sent = false" class="text-brand-pink underline decoration-4 underline-offset-2 font-black hover:text-black transition-colors">
                try a different email
              </button>
            </div>
            <NuxtLink to="/auth/login" class="inline-flex items-center gap-2 font-bold text-gray-500 hover:text-black transition-colors">
              <Icon name="ph:arrow-left" /> Back to login
            </NuxtLink>
          </div>

          <!-- Back -->
          <div class="text-center mt-6 pt-6 border-t-4 border-black">
            <NuxtLink to="/auth/login" class="inline-flex items-center gap-2 font-bold text-gray-500 hover:text-black transition-colors">
              <Icon name="ph:arrow-left" /> Back to login
            </NuxtLink>
          </div>
        </div>
      </div>
    </main>

    <Footer />
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default',
})

const email = ref('')
const sent = ref(false)

async function handleSubmit() {
  // In production, call the API
  // placeholder: show success state
  sent.value = true
}

useSeoMeta({
  title: 'Forgot Password — Linkto',
})
</script>
