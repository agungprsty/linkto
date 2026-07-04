<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
const route = useRoute()

// Initialize auth state on app mount (skip on auth pages)
const { initAuth } = useAuth()
onMounted(() => {
  if (!route.path.startsWith('/auth')) {
    initAuth()
  }
})
</script>
