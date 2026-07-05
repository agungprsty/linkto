<template>
  <BioPageContent
    :username="username"
    :profile="data?.profile || null"
    :links="data?.links || []"
    :theme="data?.theme || null"
    :loading="loading"
    :error="error"
    :show-join-link="true"
    @click="trackClick"
  />
</template>

<script setup lang="ts">
import type { BioData } from '~/types'

definePageMeta({
  layout: false,
})

const route = useRoute()
const { $api } = useNuxtApp()

const username = computed(() => route.params.username as string)
const loading = ref(true)
const error = ref<string | null>(null)
const data = ref<BioData | null>(null)

// Fetch bio data (SSR)
const { data: bioData, error: bioError } = await useAsyncData<BioData>(
  `bio-${route.params.username}`,
  async () => {
    const result = await $api(`/bio/${route.params.username}`)
    return result as BioData
  },
  {
    server: true,
    lazy: false,
  },
)

watchEffect(() => {
  if (bioData.value) {
    data.value = bioData.value
    loading.value = false
  }
  if (bioError.value) {
    error.value = 'User not found'
    loading.value = false
  }
})

// Track page view on mount
onMounted(() => {
  trackPageView()
})

function trackPageView() {
  const payload = {
    username: route.params.username as string,
    referrer: document.referrer || 'direct',
    user_agent: navigator.userAgent,
    device: /Mobi|Android/i.test(navigator.userAgent) ? 'mobile' : 'desktop',
  }
  // Fire and forget
  $api('/track/view', { method: 'POST', body: payload }).catch(() => {})
}

function trackClick(linkId: string) {
  const payload = {
    username: route.params.username as string,
    link_id: linkId,
    timestamp: new Date().toISOString(),
    page_url: window.location.href,
  }
  $api('/track/click', { method: 'POST', body: payload }).catch(() => {})
}

// SEO
const title = computed(() => `${data.value?.profile?.full_name || username.value} | Linkto`)
const description = computed(() => data.value?.profile?.bio || `Check out ${username.value} on Linkto`)

useSeoMeta({
  title,
  ogTitle: title,
  description,
  ogDescription: description,
  ogImage: computed(() => data.value?.profile?.avatar_url || undefined),
  twitterCard: 'summary_large_image',
})
</script>
