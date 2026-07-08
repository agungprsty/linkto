<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
// Initialize auth state on app mount
const { initAuth } = useAuth()
onMounted(() => {
  initAuth()
})
</script>
