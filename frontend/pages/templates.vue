<template>
  <div>
    <main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-16">
        <h1 class="text-5xl md:text-6xl font-black">Templates</h1>
        <p class="text-lg font-semibold text-gray-500 mt-4 max-w-2xl mx-auto">Choose from our collection of stunning templates. Start with a professional design and make it your own.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="tpl in templates" :key="tpl.name"
          class="bg-white border-4 border-black shadow-brutal hover:shadow-brutal-lg hover:-translate-y-2 transition-all overflow-hidden group">
          <div :class="`h-48 ${tpl.gradient} border-b-4 border-black flex items-center justify-center relative`">
            <div class="w-20 h-20 bg-white border-4 border-black rounded-full shadow-brutal-sm flex items-center justify-center z-10">
              <Icon :name="tpl.icon" class="text-3xl font-bold" />
            </div>
            <span v-if="tpl.badge" :class="`absolute top-3 right-3 ${tpl.badgeBg} text-black text-xs font-bold px-3 py-1 rounded-full border-2 border-black`">
              {{ tpl.badge }}
            </span>
          </div>
          <div class="p-6">
            <h3 class="font-black text-xl mb-2">{{ tpl.name }}</h3>
            <p class="font-semibold text-gray-600 text-sm mb-4">{{ tpl.description }}</p>
            <div class="flex flex-wrap gap-2 mb-4">
              <span v-for="tag in tpl.tags" :key="tag"
                class="text-xs font-bold bg-gray-100 px-2 py-1 rounded-full">{{ tag }}</span>
            </div>
            <NuxtLink to="/auth/register"
              class="block w-full text-center bg-black text-white font-bold py-3 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
              Use This Template
            </NuxtLink>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const templates = [
  { name: 'Storefront', badge: 'Popular', badgeBg: 'bg-brand-green', gradient: 'bg-gradient-to-br from-brand-yellow to-brand-pink', icon: 'ph:storefront', description: 'Perfect for affiliates and e-commerce. Showcase products with a visual grid layout.', tags: ['E-commerce', 'Affiliate', 'Products'] },
  { name: 'Minimalist', badge: 'Clean', badgeBg: 'bg-brand-yellow', gradient: 'bg-gradient-to-br from-brand-blue to-brand-green', icon: 'ph:user-circle', description: 'Clean and minimal design for creators who want their content to speak first.', tags: ['Clean', 'Minimal', 'Content'] },
  { name: 'Ultimate', badge: 'Pro', badgeBg: 'bg-brand-pink text-white', gradient: 'bg-gradient-to-br from-brand-pink to-brand-blue', icon: 'ph:megaphone', description: 'Full-featured layout with video, products, social feeds, and advanced blocks.', tags: ['Premium', 'All-in-one', 'Video'] },
  { name: 'Link-in-Bio Classic', badge: '', badgeBg: '', gradient: 'bg-gradient-to-br from-brand-green to-brand-yellow', icon: 'ph:link-simple', description: 'The classic link-in-bio layout optimized for maximum click-through rates.', tags: ['Classic', 'Simple', 'High CTR'] },
  { name: 'Portfolio', badge: '', badgeBg: '', gradient: 'bg-gradient-to-br from-brand-blue to-brand-pink', icon: 'ph:folder', description: 'Showcase your work with a beautiful portfolio layout. Great for designers and photographers.', tags: ['Portfolio', 'Visual', 'Creative'] },
  { name: 'SaaS Landing', badge: 'New', badgeBg: 'bg-brand-blue text-white', gradient: 'bg-gradient-to-br from-brand-pink to-brand-yellow', icon: 'ph:code', description: 'Built for indie hackers and SaaS founders to showcase products and collect waitlist signups.', tags: ['SaaS', 'Waitlist', 'Product'] },
]

useSeoMeta({ title: 'Templates — Linkto' })
</script>
