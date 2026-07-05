<template>
  <div>
    <main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-12">
        <h1 class="text-5xl md:text-6xl font-black">The Linkto Blog</h1>
        <p class="text-lg font-semibold text-gray-500 mt-4 max-w-2xl mx-auto">Tips, tricks, and insights for creators, affiliates, and brands.</p>
      </div>

      <!-- Featured Post -->
      <div class="bg-white border-4 border-black shadow-brutal mb-12 overflow-hidden hover:shadow-brutal-lg hover:-translate-y-1 transition-all">
        <div class="md:grid md:grid-cols-2">
          <div class="h-48 md:h-auto bg-gradient-to-br from-brand-yellow to-brand-pink flex items-center justify-center">
            <Icon name="ph:star" class="text-6xl text-white" />
          </div>
          <div class="p-8 flex flex-col justify-center">
            <span class="text-xs font-bold bg-brand-pink text-white px-2 py-1 rounded-full self-start mb-3">Featured</span>
            <h2 class="text-3xl font-black mb-3">The Ultimate Guide to Affiliate Marketing in 2026</h2>
            <p class="font-semibold text-gray-600 mb-4">Learn how top creators are making $10k+/month with strategic affiliate marketing through their Linkto pages.</p>
            <div class="flex items-center gap-3 text-sm font-bold text-gray-500">
              <span>By Sarah Chen</span>
              <span>•</span>
              <span>Jan 15, 2026</span>
              <span>•</span>
              <span>8 min read</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Blog Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <article v-for="post in posts" :key="post.title"
          class="bg-white border-4 border-black shadow-brutal-sm hover:shadow-brutal hover:-translate-y-2 transition-all overflow-hidden group">
          <div :class="`h-40 ${post.gradient} flex items-center justify-center`">
            <Icon :name="post.icon" class="text-4xl text-white" />
          </div>
          <div class="p-6">
            <span class="text-xs font-bold px-2 py-1 rounded-full" :class="post.tagClass">{{ post.tag }}</span>
            <h3 class="font-black text-lg mt-3 mb-2">{{ post.title }}</h3>
            <p class="font-semibold text-gray-600 text-sm">{{ post.excerpt }}</p>
            <div class="flex items-center gap-3 mt-4 text-xs font-bold text-gray-400">
              <span>{{ post.author }}</span>
              <span>•</span>
              <span>{{ post.date }}</span>
            </div>
          </div>
        </article>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const posts = [
  { title: '10 Ways to Optimize Your Link-in-Bio for Conversions', excerpt: 'Increase your click-through rate with these proven strategies.', icon: 'ph:trend-up', gradient: 'bg-gradient-to-br from-brand-blue to-brand-green', tag: 'Tips', tagClass: 'bg-brand-green text-black', author: 'Marcus Rivera', date: 'Jan 10, 2026' },
  { title: 'How to Build Your Personal Brand Online', excerpt: 'A step-by-step guide to establishing a strong online presence.', icon: 'ph:user-circle', gradient: 'bg-gradient-to-br from-brand-pink to-brand-blue', tag: 'Branding', tagClass: 'bg-brand-pink text-white', author: 'Priya Sharma', date: 'Jan 5, 2026' },
  { title: 'Analytics Deep Dive: Understanding Your Audience', excerpt: 'Make data-driven decisions with Linkto analytics.', icon: 'ph:chart-bar', gradient: 'bg-gradient-to-br from-brand-yellow to-brand-pink', tag: 'Analytics', tagClass: 'bg-brand-yellow text-black', author: 'Agung Prastyo', date: 'Dec 28, 2025' },
  { title: 'Monetize Your Content with Affiliate Products', excerpt: 'Turn your influence into income with smart affiliate strategies.', icon: 'ph:currency-dollar', gradient: 'bg-gradient-to-br from-brand-green to-brand-yellow', tag: 'Monetization', tagClass: 'bg-brand-green text-black', author: 'Sarah Chen', date: 'Dec 20, 2025' },
  { title: 'Design Trends: Neo Brutalism in Web Design', excerpt: 'Why the bold, raw aesthetic is taking over the web.', icon: 'ph:paint-roller', gradient: 'bg-gradient-to-br from-brand-blue to-brand-pink', tag: 'Design', tagClass: 'bg-brand-blue text-white', author: 'Priya Sharma', date: 'Dec 15, 2025' },
  { title: 'Getting Started with Linkto: A Complete Guide', excerpt: 'Everything you need to know to set up your first Linkto page.', icon: 'ph:rocket', gradient: 'bg-gradient-to-br from-brand-pink to-brand-yellow', tag: 'Getting Started', tagClass: 'bg-brand-pink text-white', author: 'Marcus Rivera', date: 'Dec 10, 2025' },
]

useSeoMeta({ title: 'Blog — Linkto' })
</script>
