<template>
  <nav class="fixed top-0 w-full bg-brand-bg border-b-4 border-black z-50">
    <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-20 items-center">
        <!-- Logo -->
        <NuxtLink to="/" class="flex-shrink-0 flex items-center gap-2 cursor-pointer">
          <div class="w-10 h-10 bg-black rounded-full flex items-center justify-center -rotate-12 hover:rotate-0 transition-transform">
            <Icon name="ph:link" class="text-brand-yellow text-2xl font-bold" />
          </div>
          <span class="font-black text-3xl tracking-tight">Linkto.</span>
        </NuxtLink>

        <!-- Desktop Menu -->
        <div class="hidden xl:flex items-center gap-8 font-bold text-lg">
          <a href="/#features" class="hover:text-brand-pink hover:underline decoration-4 underline-offset-4 transition-colors">Features</a>
          <a href="/#templates" class="hover:text-brand-blue hover:underline decoration-4 underline-offset-4 transition-colors">Templates</a>
          <a href="/#pricing" class="hover:text-brand-green hover:underline decoration-4 underline-offset-4 transition-colors">Pricing</a>
          <a href="/#reviews" class="hover:text-brand-pink hover:underline decoration-4 underline-offset-4 transition-colors">Reviews</a>
          <a href="/#faq" class="hover:text-brand-blue hover:underline decoration-4 underline-offset-4 transition-colors">FAQ</a>
        </div>

        <!-- Right Actions -->
        <div class="flex items-center gap-4">
          <template v-if="isAuthenticated">
            <NuxtLink to="/dashboard" class="bg-black text-white font-bold text-base md:text-lg px-6 py-3 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full flex items-center gap-2">
              <Icon name="ph:layout" class="font-bold" />
              Dashboard
            </NuxtLink>
          </template>
          <template v-else>
            <NuxtLink to="/auth/login" class="hidden md:block font-bold text-lg hover:underline decoration-4 underline-offset-4 bg-white border-2 border-transparent px-4 py-2 hover:border-black rounded-lg transition-all">
              Log in
            </NuxtLink>
            <NuxtLink to="/auth/register" class="bg-black text-white font-bold text-base md:text-lg px-6 py-3 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full flex items-center gap-2">
              Sign Up Free <Icon name="ph:arrow-right" class="font-bold" />
            </NuxtLink>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
const { isAuthenticated } = useAuth()
</script>
