<template>
  <div class="min-h-screen bg-brand-bg flex items-center justify-center px-4">
    <div class="text-center max-w-lg">
      <div class="text-8xl font-black mb-4">{{ error?.statusCode || '404' }}</div>
      <h1 class="text-4xl font-black mb-4">
        {{ error?.statusCode === 404 ? 'Page not found' : 'Something went wrong' }}
      </h1>
      <p class="text-lg font-semibold text-gray-600 mb-8">
        {{ error?.statusCode === 404 ? 'The page you\'re looking for doesn\'t exist.' : 'An unexpected error occurred. Please try again.' }}
      </p>
      <div class="flex gap-4 justify-center">
        <NuxtLink to="/"
          class="bg-black text-white font-bold px-8 py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
          Go Home
        </NuxtLink>
        <button @click="handleError"
          class="bg-white text-black font-bold px-8 py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
          Try Again
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  error: {
    type: Object,
    default: null,
  },
})

const handleError = () => clearError({ redirect: '/' })

useSeoMeta({
  title: props.error?.statusCode === 404 ? 'Page Not Found — Linkto' : 'Error — Linkto',
})
</script>
