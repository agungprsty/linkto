<template>
  <div>
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-12">
        <h1 class="text-5xl md:text-6xl font-black">Help Center</h1>
        <p class="text-lg font-semibold text-gray-500 mt-4 max-w-2xl mx-auto">Find answers to common questions. Can't find what you're looking for? Reach out to our support team.</p>
      </div>

      <!-- Search -->
      <div class="max-w-xl mx-auto mb-12">
        <div class="flex border-4 border-black shadow-brutal-sm focus-within:shadow-brutal focus-within:translate-x-[2px] focus-within:translate-y-[2px] transition-all">
          <span class="inline-flex items-center px-4 bg-gray-100 font-bold text-gray-500 border-r-4 border-black">
            <Icon name="ph:magnifying-glass" class="text-xl" />
          </span>
          <input v-model="search" type="text" placeholder="Search for help articles..."
            class="flex-1 py-4 px-4 font-semibold text-base bg-white outline-none border-0">
        </div>
      </div>

      <!-- Categories -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-12">
        <NuxtLink v-for="cat in categories" :key="cat.title" to="#"
          class="bg-white border-4 border-black shadow-brutal-sm p-5 text-center hover:shadow-brutal hover:-translate-y-1 transition-all">
          <div :class="`w-12 h-12 ${cat.bg} border-4 border-black rounded-full flex items-center justify-center mx-auto mb-3 ${cat.rotation}`">
            <Icon :name="cat.icon" class="text-xl font-bold" />
          </div>
          <h3 class="font-black text-sm">{{ cat.title }}</h3>
        </NuxtLink>
      </div>

      <!-- FAQ -->
      <h2 class="text-3xl font-black text-center mb-8 bg-white border-4 border-black px-6 py-3 shadow-brutal-sm inline-block mx-auto -rotate-1 hover:rotate-0 transition-transform">Frequently Asked Questions</h2>

      <div class="space-y-4 mt-8">
        <div v-for="(faq, i) in filteredFaqs" :key="i"
          class="bg-white border-4 border-black shadow-brutal-sm overflow-hidden">
          <details class="group">
            <summary class="flex items-center justify-between p-6 font-black text-lg cursor-pointer hover:bg-gray-50 transition-colors list-none">
              {{ faq.q }}
              <Icon name="ph:caret-down" class="text-2xl group-open:rotate-180 transition-transform" />
            </summary>
            <div class="px-6 pb-6 border-t-4 border-black pt-4">
              <p class="font-semibold text-gray-700 leading-relaxed" v-html="faq.a" />
            </div>
          </details>
        </div>
      </div>

      <!-- Contact -->
      <div class="bg-white border-4 border-black shadow-brutal p-8 mt-12 text-center">
        <div class="w-16 h-16 bg-brand-pink border-4 border-black rounded-full flex items-center justify-center mx-auto mb-5 -rotate-6">
          <Icon name="ph:headset" class="text-3xl font-bold" />
        </div>
        <h2 class="text-3xl font-black mb-3">Still need help?</h2>
        <p class="font-semibold text-gray-600 mb-6 max-w-lg mx-auto">Our support team typically responds within 2 hours during business hours.</p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="mailto:support@linkto.com"
            class="bg-black text-white font-black text-base px-8 py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full inline-flex items-center gap-2">
            <Icon name="ph:envelope-simple" class="text-lg" /> Email Support
          </a>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const search = ref('')

const categories = [
  { title: 'Getting Started', icon: 'ph:rocket', bg: 'bg-brand-yellow', rotation: '-rotate-6' },
  { title: 'Managing Links', icon: 'ph:link', bg: 'bg-brand-pink', rotation: 'rotate-3' },
  { title: 'Analytics', icon: 'ph:chart-line-up', bg: 'bg-brand-blue', rotation: '-rotate-3' },
  { title: 'Billing & Plans', icon: 'ph:currency-dollar', bg: 'bg-brand-green', rotation: 'rotate-6' },
]

const faqs = [
  { q: 'How do I create a Linkto account?', a: 'Creating an account is free and takes less than 60 seconds. Click "Sign Up Free" in the top right corner, enter your email and create a password, or sign up instantly with Google or Apple. Once registered, you can immediately start customizing your Linkto page.' },
  { q: 'How do I add affiliate products to my page?', a: 'With our Smart Affiliate Scraper, you can paste a product link from supported marketplaces (Shopee, Tokopedia, Amazon, etc.) directly into the "Add Product" button in your dashboard. We\'ll automatically fetch the image, title, and price.' },
  { q: 'Can I use my own custom domain?', a: 'Yes! Custom domains are available on the Pro plan and above. Simply go to your Settings > Custom Domain, enter your domain, and update your DNS records.' },
  { q: 'How do I cancel my subscription?', a: 'You can cancel your subscription anytime from your dashboard under Settings > Billing. Your paid features will remain active until the end of your current billing period.' },
  { q: 'How do I track my link clicks and analytics?', a: 'Analytics are available on all plans. You can view your stats by clicking on "Analytics" in the dashboard sidebar.' },
  { q: 'Is my data safe with Linkto?', a: 'Absolutely. We use industry-standard encryption and security measures to protect your data. We never sell your personal information.' },
]

const filteredFaqs = computed(() => {
  if (!search.value) return faqs
  const q = search.value.toLowerCase()
  return faqs.filter(f => f.q.toLowerCase().includes(q) || f.a.toLowerCase().includes(q))
})

useSeoMeta({ title: 'Help Center — Linkto' })
</script>
