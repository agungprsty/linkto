<template>
  <div>
    <div class="flex items-center justify-between mb-8">
      <h1 class="text-3xl font-black">Analytics</h1>
      <div class="flex gap-2">
        <button @click="period = '7d'"
          class="px-4 py-2 border-4 border-black font-bold text-sm transition-all"
          :class="period === '7d' ? 'bg-black text-white' : 'bg-white text-black hover:bg-gray-50'">7 Days</button>
        <button @click="period = '30d'"
          class="px-4 py-2 border-4 border-black font-bold text-sm transition-all"
          :class="period === '30d' ? 'bg-black text-white' : 'bg-white text-black hover:bg-gray-50'">30 Days</button>
      </div>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="text-center py-20">
      <Icon name="ph:spinner" class="animate-spin text-4xl text-gray-400 mx-auto mb-4" />
      <p class="font-semibold text-gray-500">Loading analytics...</p>
    </div>

    <!-- Stats Cards -->
    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <div class="bg-white rounded-2xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-2">
          <span class="text-sm font-bold text-gray-500">Total Views</span>
          <Icon name="ph:eye" class="text-brand-blue text-xl" />
        </div>
        <p class="text-3xl font-black">{{ summary?.total_views || 0 }}</p>
      </div>
      <div class="bg-white rounded-2xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-2">
          <span class="text-sm font-bold text-gray-500">Total Clicks</span>
          <Icon name="ph:cursor-click" class="text-brand-pink text-xl" />
        </div>
        <p class="text-3xl font-black">{{ summary?.total_clicks || 0 }}</p>
      </div>
      <div class="bg-white rounded-2xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-2">
          <span class="text-sm font-bold text-gray-500">Click Rate</span>
          <Icon name="ph:trend-up" class="text-brand-green text-xl" />
        </div>
        <p class="text-3xl font-black">{{ clickRate }}%</p>
      </div>
      <div class="bg-white rounded-2xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-2">
          <span class="text-sm font-bold text-gray-500">Links</span>
          <Icon name="ph:link" class="text-brand-yellow text-xl" />
        </div>
        <p class="text-3xl font-black">{{ linksStore.links.length }}</p>
      </div>
    </div>

    <!-- Chart Placeholder -->
    <div v-if="!loading" class="bg-white rounded-2xl border border-gray-200 p-6 mb-8">
      <h3 class="font-black text-lg mb-4">Daily Performance</h3>
      <div class="h-64 flex items-end justify-around gap-2 pt-4">
        <div v-for="(day, i) in chartDays" :key="i"
          class="flex-1 flex flex-col items-center gap-1">
          <div class="w-full rounded-t-md transition-all"
            :style="{ height: day.height + '%', backgroundColor: day.color }" />
          <span class="text-[10px] font-bold text-gray-400">{{ day.label }}</span>
        </div>
      </div>
      <div class="flex items-center justify-center gap-6 mt-4 text-sm font-semibold text-gray-500">
        <span class="flex items-center gap-2"><span class="w-3 h-3 rounded-sm bg-brand-blue" /> Views</span>
        <span class="flex items-center gap-2"><span class="w-3 h-3 rounded-sm bg-brand-pink" /> Clicks</span>
      </div>
    </div>

    <!-- Top Links -->
    <div v-if="!loading && summary?.links_stats?.length" class="bg-white rounded-2xl border border-gray-200 p-6">
      <h3 class="font-black text-lg mb-4">Top Performing Links</h3>
      <div class="space-y-3">
        <div v-for="stat in summary.links_stats" :key="stat.link_id"
          class="flex items-center justify-between p-3 bg-gray-50 rounded-xl">
          <span class="font-semibold text-sm truncate mr-4">{{ stat.title }}</span>
          <span class="font-bold text-sm whitespace-nowrap">{{ stat.clicks }} clicks</span>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else-if="!loading" class="text-center py-16">
      <div class="w-20 h-20 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
        <Icon name="ph:chart-bar" class="text-3xl text-gray-400" />
      </div>
      <h3 class="text-xl font-black mb-2">No data yet</h3>
      <p class="text-gray-500 font-semibold">Share your Linkto page to start getting analytics.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'dashboard',
  middleware: 'auth',
})

const linksStore = useLinksStore()
const { $api } = useNuxtApp()

const period = ref('7d')
const loading = ref(true)
const summary = ref<any>(null)

const chartDays = computed(() => {
  if (!summary.value?.daily_stats) return []
  const stats = summary.value.daily_stats.slice(-7)
  const maxVal = Math.max(...stats.map((s: any) => Math.max(s.views, s.clicks)), 1)

  return stats.map((day: any) => ({
    label: new Date(day.date).toLocaleDateString('en', { weekday: 'short' }),
    height: (day.views / maxVal) * 100,
    color: '#4D9FFF',
  }))
})

const clickRate = computed(() => {
  if (!summary.value?.total_views || summary.value.total_views === 0) return 0
  return ((summary.value.total_clicks / summary.value.total_views) * 100).toFixed(1)
})

async function fetchAnalytics() {
  loading.value = true
  try {
    const data = await $api('/analytics/summary', {
      params: { period: period.value },
    })
    summary.value = data
  } catch {
    // Use mock data for now
    summary.value = {
      total_views: 0,
      total_clicks: 0,
      daily_stats: [],
      links_stats: [],
    }
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchAnalytics()
  linksStore.fetchLinks()
})

watch(period, () => {
  fetchAnalytics()
})
</script>
