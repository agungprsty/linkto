<template>
  <div class="min-h-screen flex flex-col">
    <Navbar v-if="!isDashboard && !isAuth" />
    <main class="flex-1" :class="contentPadding">
      <slot />
    </main>
    <Footer v-if="!isDashboard && !isAuth" />
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const isDashboard = computed(() => route.path.startsWith('/dashboard'))
const isAuth = computed(() => route.path.startsWith('/auth'))
const isIndex = computed(() => route.path === '/')
const isBio = computed(() => {
  // Match /[username] routes (single segment, not auth, not other known pages)
  const segments = route.path.split('/').filter(Boolean)
  if (segments.length !== 1) return false
  const knownPages = ['auth', 'dashboard', 'about', 'blog', 'help', 'community', 'templates', 'terms', 'privacy', 'cookie']
  return !knownPages.includes(segments[0])
})

const contentPadding = computed(() => {
  // Landing page, auth pages, and bio pages handle their own padding
  if (isIndex.value || isAuth.value || isBio.value) return ''
  return 'pt-20'
})
</script>
