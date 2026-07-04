<template>
  <div>
    <!-- ===== HERO SECTION ===== -->
    <main class="pt-32 pb-20 px-4 sm:px-6 lg:px-8 max-w-screen-2xl mx-auto">
      <div class="flex flex-col lg:flex-row items-center gap-16 lg:gap-8 min-h-[75vh]">
        <!-- Left Content -->
        <div class="flex-1 text-center lg:text-left space-y-8 lg:pr-12">
          <h1 class="text-6xl sm:text-7xl lg:text-[5.5rem] font-black leading-[1.05] tracking-tight text-black">
            Everything <br> you are <br>
            <span class="bg-brand-yellow px-4 border-4 border-black shadow-brutal inline-block mt-4 -rotate-2 transform hover:rotate-2 transition-transform duration-300">in one link.</span>
          </h1>
          <p class="text-xl sm:text-2xl font-semibold text-gray-800 max-w-2xl mx-auto lg:mx-0">
            Join <strong class="text-brand-pink">10+ million</strong> creators, affiliates, and brands building their online hub. One link to help you share everything you create, curate and sell from your Instagram, TikTok, Facebook, YouTube and other social media profiles.
          </p>

          <!-- Stats Bar -->
          <div class="flex flex-wrap gap-6 sm:gap-10 justify-center lg:justify-start pt-4">
            <div class="text-center">
              <p class="text-3xl font-black">10M+</p>
              <p class="text-sm font-bold text-gray-500">Creators</p>
            </div>
            <div class="w-px h-12 bg-black/20 self-center" />
            <div class="text-center">
              <p class="text-3xl font-black">500M+</p>
              <p class="text-sm font-bold text-gray-500">Monthly Views</p>
            </div>
            <div class="w-px h-12 bg-black/20 self-center" />
            <div class="text-center">
              <p class="text-3xl font-black">4.9★</p>
              <p class="text-sm font-bold text-gray-500">Avg. Rating</p>
            </div>
          </div>

          <!-- Form -->
          <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start pt-6">
            <div class="flex-grow max-w-sm flex border-4 border-black shadow-brutal rounded-none bg-white transition-all focus-within:translate-x-[4px] focus-within:translate-y-[4px] focus-within:shadow-brutal-hover">
              <span class="flex items-center pl-4 pr-2 text-xl font-bold text-gray-400 pointer-events-none leading-none select-none whitespace-nowrap">linkto.com/</span>
              <input v-model="usernameSearch" type="text" placeholder="username"
                class="flex-1 min-w-0 text-xl font-bold bg-transparent border-0 py-5 pr-4 focus:outline-none focus:ring-0">
            </div>
            <NuxtLink :to="usernameSearch ? `/auth/register?username=${usernameSearch}` : '/auth/register'"
              class="bg-brand-pink text-black font-black text-xl px-10 py-5 border-4 border-black shadow-brutal hover:shadow-brutal-hover hover:translate-x-[4px] hover:translate-y-[4px] transition-all whitespace-nowrap text-center">
              Get started for free
            </NuxtLink>
          </div>
        </div>

        <!-- Right Visual -->
        <div class="flex-1 relative w-full max-w-md lg:max-w-none flex justify-center lg:justify-end">
          <div class="relative w-80 h-[580px] bg-[#E8E8E8] border-[6px] border-black rounded-[3rem] shadow-brutal-xl p-5 flex flex-col gap-4 overflow-hidden z-10 float-slow">
            <!-- Phone Notch -->
            <div class="w-32 h-6 bg-black rounded-b-2xl mx-auto absolute top-0 left-1/2 -translate-x-1/2 z-20" />

            <!-- Mock Content -->
            <div class="mt-8 flex flex-col items-center gap-3 relative z-10">
              <div class="w-28 h-28 bg-brand-blue border-4 border-black rounded-full shadow-brutal-sm overflow-hidden">
                <img src="https://api.dicebear.com/7.x/notionists/svg?seed=Agung" alt="Avatar" class="w-full h-full object-cover bg-white">
              </div>
              <h3 class="font-black text-2xl">@agung_dev</h3>
              <p class="font-bold text-sm text-center bg-white border-2 border-black px-3 py-1 rounded-full shadow-brutal-sm">Tech & Setup Reviewer</p>
              <div class="flex gap-2 mt-1">
                <div class="w-7 h-7 bg-white border-2 border-black rounded-full flex items-center justify-center text-xs font-bold">IG</div>
                <div class="w-7 h-7 bg-white border-2 border-black rounded-full flex items-center justify-center text-xs font-bold">TT</div>
                <div class="w-7 h-7 bg-white border-2 border-black rounded-full flex items-center justify-center text-xs font-bold">YT</div>
              </div>
            </div>

            <!-- Mock Links -->
            <div class="flex-1 flex flex-col gap-3 mt-4 relative z-10 w-full overflow-y-auto no-scrollbar pb-6">
              <div class="w-full bg-white border-4 border-black shadow-brutal-sm p-3 font-bold text-center hover:-translate-y-1 transition-transform cursor-pointer flex items-center justify-center gap-2">
                <Icon name="ph:play-circle" class="text-brand-pink text-lg" /> My Setup Tour (YouTube)
              </div>
              <div class="w-full bg-brand-green border-4 border-black shadow-brutal-sm p-3 font-bold text-center hover:-translate-y-1 transition-transform cursor-pointer flex items-center justify-center gap-2">
                <Icon name="ph:shopping-bag" class="text-lg" /> Shop My Gear
              </div>

              <div class="grid grid-cols-2 gap-3 mt-2">
                <div class="bg-brand-yellow border-4 border-black shadow-brutal-sm flex flex-col aspect-square overflow-hidden hover:-translate-y-1 transition-transform cursor-pointer">
                  <div class="h-1/2 bg-white border-b-4 border-black flex items-center justify-center p-2">
                    <div class="w-full h-full bg-gray-200 rounded-sm flex items-center justify-center font-bold text-gray-400">📷</div>
                  </div>
                  <div class="p-2 flex-1 flex items-center justify-center text-center font-bold text-[10px] leading-tight">Mechanical Keyboard</div>
                </div>
                <div class="bg-brand-pink border-4 border-black shadow-brutal-sm flex flex-col aspect-square overflow-hidden hover:-translate-y-1 transition-transform cursor-pointer">
                  <div class="h-1/2 bg-white border-b-4 border-black flex items-center justify-center p-2">
                    <div class="w-full h-full bg-gray-200 rounded-sm flex items-center justify-center font-bold text-gray-400">🎧</div>
                  </div>
                  <div class="p-2 flex-1 flex items-center justify-center text-center font-bold text-[10px] leading-tight">Monitor Lightbar</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Decorative Elements -->
          <div class="absolute top-10 -right-4 lg:right-10 w-24 h-24 bg-brand-yellow border-4 border-black rounded-full shadow-brutal z-20 flex items-center justify-center -rotate-12">
            <span class="font-black text-2xl">#1</span>
          </div>
          <div class="absolute -bottom-6 -left-4 lg:left-6 w-32 h-32 bg-brand-green border-4 border-black shadow-brutal rotate-12 -z-0 flex items-center justify-center">
            <Icon name="ph:lightning" class="text-5xl font-bold" />
          </div>
          <div class="absolute bottom-20 -right-8 w-16 h-16 bg-brand-pink border-4 border-black shadow-brutal-sm rounded-full -z-0" />
        </div>
      </div>
    </main>

    <!-- ===== MARQUEE ===== -->
    <section class="border-y-4 border-black bg-black py-8 overflow-hidden">
      <div class="flex whitespace-nowrap animate-marquee">
        <div class="flex items-center gap-16 mx-8">
          <span class="text-white font-black text-2xl flex items-center gap-3"><Icon name="ph:lightning" class="text-brand-yellow" /> 10M+ Creators Worldwide</span>
          <span class="text-white font-black text-2xl flex items-center gap-3"><Icon name="ph:globe" class="text-brand-blue" /> 195+ Countries</span>
          <span class="text-white font-black text-2xl flex items-center gap-3"><Icon name="ph:link" class="text-brand-green" /> 500M+ Links Shared</span>
          <span class="text-white font-black text-2xl flex items-center gap-3"><Icon name="ph:currency-dollar" class="text-brand-pink" /> $50M+ Affiliates Earned</span>
        </div>
        <div class="flex items-center gap-16 mx-8">
          <span class="text-white font-black text-2xl flex items-center gap-3"><Icon name="ph:lightning" class="text-brand-yellow" /> 10M+ Creators Worldwide</span>
          <span class="text-white font-black text-2xl flex items-center gap-3"><Icon name="ph:globe" class="text-brand-blue" /> 195+ Countries</span>
          <span class="text-white font-black text-2xl flex items-center gap-3"><Icon name="ph:link" class="text-brand-green" /> 500M+ Links Shared</span>
          <span class="text-white font-black text-2xl flex items-center gap-3"><Icon name="ph:currency-dollar" class="text-brand-pink" /> $50M+ Affiliates Earned</span>
        </div>
      </div>
    </section>

    <!-- ===== FEATURES ===== -->
    <section id="features" class="bg-brand-bg border-b-4 border-black py-24 relative overflow-hidden">
      <div class="absolute top-20 right-20 w-64 h-64 bg-brand-yellow/20 border-4 border-black rounded-full -z-0" />
      <div class="absolute bottom-20 left-20 w-48 h-48 bg-brand-blue/20 border-4 border-black -z-0 rotate-12" />

      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="text-center mb-20">
          <h2 class="text-4xl md:text-6xl font-black text-black inline-block bg-white border-4 border-black px-6 py-3 shadow-brutal -rotate-1 hover:rotate-0 transition-transform">
            More Than Just Links
          </h2>
          <p class="text-xl font-semibold text-gray-600 mt-6 max-w-2xl mx-auto">Everything you need to grow your audience and monetize your presence — all from one link.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="feature in features" :key="feature.title"
            class="bg-white border-4 border-black p-8 shadow-brutal hover:shadow-brutal-lg hover:-translate-y-2 transition-all group">
            <div :class="`w-16 h-16 ${feature.iconBg} border-4 border-black rounded-full flex items-center justify-center mb-6 shadow-brutal-sm ${feature.rotation} group-hover:rotate-0 transition-transform`">
              <Icon :name="feature.icon" class="text-3xl font-bold" />
            </div>
            <h3 class="text-2xl font-black mb-4">{{ feature.title }}</h3>
            <p class="font-semibold text-gray-700 text-lg leading-relaxed">{{ feature.description }}</p>
            <NuxtLink to="/about" class="mt-6 inline-flex items-center gap-2 font-bold text-black hover:text-brand-pink transition-colors">
              Learn more <Icon name="ph:arrow-right" />
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== TEMPLATES ===== -->
    <section id="templates" class="bg-brand-bg border-b-4 border-black py-24">
      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-6xl font-black text-black inline-block bg-white border-4 border-black px-6 py-3 shadow-brutal rotate-1 hover:rotate-0 transition-transform">
            Stunning Templates
          </h2>
          <p class="text-xl font-semibold text-gray-600 mt-6 max-w-2xl mx-auto">Start with a professional design and make it your own. No coding required.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div v-for="tpl in templates" :key="tpl.title"
            class="bg-white border-4 border-black shadow-brutal hover:shadow-brutal-lg hover:-translate-y-2 transition-all overflow-hidden group">
            <div :class="`h-48 ${tpl.gradient} border-b-4 border-black flex items-center justify-center relative overflow-hidden`">
              <div class="w-20 h-20 bg-white border-4 border-black rounded-full shadow-brutal-sm flex items-center justify-center z-10">
                <Icon :name="tpl.icon" class="text-3xl font-bold" />
              </div>
              <div :class="`absolute ${tpl.decoClass}`" />
            </div>
            <div class="p-6">
              <div class="flex items-center justify-between mb-3">
                <h3 class="font-black text-xl">{{ tpl.title }}</h3>
                <span :class="`${tpl.badgeBg} text-black text-xs font-bold px-2 py-1 rounded-full`">{{ tpl.badge }}</span>
              </div>
              <p class="font-semibold text-gray-600">{{ tpl.description }}</p>
            </div>
          </div>
        </div>

        <div class="text-center mt-12">
          <NuxtLink to="/templates" class="inline-flex items-center gap-2 bg-black text-white font-black text-lg px-8 py-4 border-4 border-black shadow-brutal hover:shadow-brutal-hover hover:translate-x-[4px] hover:translate-y-[4px] transition-all">
            Browse All Templates <Icon name="ph:arrow-right" />
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- ===== PRICING ===== -->
    <section id="pricing" class="bg-brand-bg border-b-4 border-black py-24 relative overflow-hidden">
      <div class="absolute top-1/2 left-0 w-full h-2 bg-black -translate-y-1/2 -z-0" />

      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-6xl font-black text-black inline-block bg-white border-4 border-black px-6 py-3 shadow-brutal -rotate-2 hover:rotate-0 transition-transform">
            Choose Your Plan
          </h2>
          <p class="text-xl font-semibold text-gray-600 mt-6 max-w-2xl mx-auto">Start free. Upgrade when you grow. No hidden fees, no surprises.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div v-for="plan in pricing" :key="plan.name"
            class="bg-white border-4 border-black shadow-brutal hover:shadow-brutal-lg hover:-translate-y-2 transition-all p-8 relative">
            <div v-if="plan.badge" :class="`absolute -top-3 -right-3 ${plan.badgeBg} border-3 border-black px-3 py-1 font-black text-sm shadow-brutal-sm`">{{ plan.badge }}</div>
            <div class="text-center">
              <h3 class="text-2xl font-black mb-2">{{ plan.name }}</h3>
              <p class="text-5xl font-black mb-2">{{ plan.price }}</p>
              <p class="text-sm font-bold text-gray-500 mb-6">{{ plan.period }}</p>
              <ul class="text-left space-y-4 mb-8">
                <li v-for="feature in plan.features" :key="feature.text"
                  class="flex items-start gap-3 font-semibold"
                  :class="feature.included ? '' : 'text-gray-400'">
                  <Icon v-if="feature.included" name="ph:check-circle" class="text-brand-green text-xl flex-shrink-0 mt-0.5" />
                  <Icon v-else name="ph:x-circle" class="text-xl flex-shrink-0 mt-0.5" />
                  {{ feature.text }}
                </li>
              </ul>
              <NuxtLink to="/auth/register"
                class="block w-full font-bold text-lg py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all text-center"
                :class="plan.ctaClass">
                {{ plan.cta }}
              </NuxtLink>
            </div>
          </div>
        </div>

        <div class="text-center mt-12">
          <p class="font-bold text-gray-500">All plans include a 14-day free trial. No credit card required.</p>
        </div>
      </div>
    </section>

    <!-- ===== REVIEWS ===== -->
    <section id="reviews" class="bg-brand-bg border-b-4 border-black py-24 relative overflow-hidden">
      <div class="absolute -top-20 -right-20 w-80 h-80 bg-brand-pink/10 border-4 border-black rounded-full -z-0" />
      <div class="absolute -bottom-20 -left-20 w-80 h-80 bg-brand-blue/10 border-4 border-black rounded-full -z-0" />

      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-6xl font-black text-black inline-block bg-white border-4 border-black px-6 py-3 shadow-brutal rotate-1 hover:rotate-0 transition-transform">
            Loved by Creators Worldwide
          </h2>
          <p class="text-xl font-semibold text-gray-600 mt-6 max-w-2xl mx-auto">Join millions of satisfied creators who trust Linkto to power their online presence.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="review in reviews" :key="review.name"
            class="review-card visible bg-white border-4 border-black p-8 shadow-brutal hover:shadow-brutal-lg hover:-translate-y-2 transition-all">
            <div class="flex items-center gap-1 mb-4">
              <Icon v-for="i in 5" :key="i" name="ph:star" class="text-brand-yellow text-xl" />
            </div>
            <p class="text-lg font-semibold text-gray-700 leading-relaxed mb-6">"{{ review.text }}"</p>
            <div class="flex items-center gap-4">
              <div :class="`w-14 h-14 ${review.avatarBg} border-3 border-black rounded-full overflow-hidden flex-shrink-0`">
                <img :src="`https://api.dicebear.com/7.x/notionists/svg?seed=${review.name}`" :alt="review.name" class="w-full h-full object-cover">
              </div>
              <div>
                <p class="font-black text-lg">{{ review.name }}</p>
                <p class="font-bold text-sm text-gray-500">{{ review.role }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== FAQ ===== -->
    <section id="faq" class="bg-brand-bg border-b-4 border-black py-24">
      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-6xl font-black text-black inline-block bg-white border-4 border-black px-6 py-3 shadow-brutal -rotate-1 hover:rotate-0 transition-transform">
            Got Questions?
          </h2>
          <p class="text-xl font-semibold text-gray-600 mt-6 max-w-2xl mx-auto">Everything you need to know about Linkto. Can't find what you're looking for? <NuxtLink to="/help" class="text-brand-pink underline">Contact our team</NuxtLink>.</p>
        </div>

        <div class="max-w-3xl mx-auto space-y-6">
          <div v-for="(item, i) in faqs" :key="i"
            class="bg-white border-4 border-black shadow-brutal-sm overflow-hidden">
            <details class="group">
              <summary class="flex items-center justify-between p-6 font-black text-xl cursor-pointer hover:bg-gray-50 transition-colors list-none">
                {{ item.q }}
                <Icon name="ph:caret-down" class="text-2xl group-open:rotate-180 transition-transform" />
              </summary>
              <div class="px-6 pb-6 border-t-4 border-black pt-4">
                <p class="font-semibold text-gray-700 text-lg leading-relaxed">{{ item.a }}</p>
              </div>
            </details>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== CTA ===== -->
    <section id="cta" class="bg-brand-yellow border-b-4 border-black py-24 relative overflow-hidden">
      <!-- Decorative elements -->
      <div class="absolute top-10 left-10 w-32 h-32 bg-black rounded-full -z-0 float-slow" />
      <div class="absolute bottom-10 right-10 w-48 h-48 bg-white border-4 border-black -z-0 rotate-12" />
      <div class="absolute top-1/2 right-1/4 w-16 h-16 bg-brand-pink border-4 border-black rounded-full -z-0" />

      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
        <h2 class="text-5xl md:text-7xl font-black text-black leading-[1.1] max-w-4xl mx-auto">
          Ready to put<br>
          <span class="bg-white px-4 border-4 border-black shadow-brutal inline-block mt-4 -rotate-1">everything in one link?</span>
        </h2>
        <p class="text-xl md:text-2xl font-bold text-black/70 mt-8 max-w-2xl mx-auto">Join 10+ million creators already using Linkto. It's free to start, takes 60 seconds to set up.</p>

        <div class="flex flex-col sm:flex-row gap-4 justify-center mt-10">
          <div class="flex-grow max-w-sm mx-auto sm:mx-0 flex border-4 border-black shadow-brutal rounded-none bg-white transition-all focus-within:translate-x-[4px] focus-within:translate-y-[4px] focus-within:shadow-brutal-hover">
            <span class="flex items-center pl-4 pr-2 text-lg font-bold text-gray-400 pointer-events-none leading-none select-none whitespace-nowrap">linkto.com/</span>
            <input v-model="ctaUsername" type="text" placeholder="username"
              class="flex-1 min-w-0 text-lg font-bold bg-transparent border-0 py-4 pr-4 focus:outline-none focus:ring-0">
          </div>
          <NuxtLink :to="ctaUsername ? `/auth/register?username=${ctaUsername}` : '/auth/register'"
            class="bg-black text-white font-black text-xl px-10 py-4 border-4 border-black shadow-brutal hover:shadow-brutal-hover hover:translate-x-[4px] hover:translate-y-[4px] transition-all whitespace-nowrap">
            Create Your Linkto
          </NuxtLink>
        </div>
        <p class="text-sm font-bold text-black/50 mt-4">No credit card required • Free forever plan • 60 seconds setup</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const usernameSearch = ref('')
const ctaUsername = ref('')

const faqs = [
  { q: 'What is Linkto?', a: 'Linkto is the ultimate link-in-bio platform designed for creators, affiliates, and businesses. Unlike traditional link-in-bio tools, Linkto combines beautiful Neo Brutalism design with powerful monetization features — including an affiliate product hub, deep analytics, and custom domains. It\'s everything you are, in one link.' },
  { q: 'Is Linkto really free?', a: 'Yes! Our Free plan includes unlimited links, basic analytics, and one theme — forever. No time limit, no credit card required. When you\'re ready to grow, you can upgrade to Starter ($5/mo), Pro ($12/mo), or Premium ($24/mo) for advanced features like custom domains, monetization tools, and priority support.' },
  { q: 'Can I use my own domain?', a: 'Absolutely! Custom domains are available on the Pro plan and above. Connect your own domain (like link.username.com) to your Linkto page — it takes less than 5 minutes to set up with our simple DNS configuration guide.' },
  { q: 'How does the Affiliate Hub work?', a: 'The Affiliate Hub lets you create a visual storefront directly on your Linkto page. Simply paste a product link from supported marketplaces (Shopee, Tokopedia, Amazon, etc.) and our smart auto-scraper will fetch the image, title, and price automatically. You can organize products into categories, set custom prices, and track conversions — all from one dashboard.' },
  { q: 'Can I migrate from another platform?', a: 'Yes! We offer a one-click import tool that lets you migrate your links from Linktree, Bio.link, and other major platforms. Your links, themes, and settings transfer seamlessly. Most users complete the migration in under 2 minutes.' },
  { q: 'What kind of analytics do you provide?', a: 'Our analytics dashboard tracks page views, link clicks, click-through rates, traffic sources, geographic data, and device information. Pro and Premium plans unlock advanced analytics including conversion tracking, revenue attribution, custom date ranges, and exportable reports.' },
]

const features = [
  { title: 'Affiliate Hub Built-In', description: "Don't just share links. Build a visual storefront. Add products directly from marketplaces with our smart auto-scraper.", icon: 'ph:shopping-bag', iconBg: 'bg-brand-pink', rotation: '-rotate-6' },
  { title: 'Deep Analytics', description: 'Track what converts. See real-time clicks, views, and revenue. Integrate Meta & TikTok Pixels for advanced retargeting.', icon: 'ph:chart-line-up', iconBg: 'bg-brand-yellow', rotation: 'rotate-3' },
  { title: 'Radical Customization', description: 'Your brand, your rules. Custom domains, dynamic themes, custom fonts, and Neo-Brutalist components available.', icon: 'ph:paint-roller', iconBg: 'bg-brand-green', rotation: '-rotate-3' },
  { title: 'Smart Link Scheduling', description: 'Schedule links to publish and unpublish automatically. Perfect for product launches, promotions, and time-sensitive campaigns.', icon: 'ph:link-simple', iconBg: 'bg-brand-blue', rotation: 'rotate-6' },
  { title: 'Monetization Tools', description: 'Accept tips, sell products, and grow memberships directly from your Linkto page. No middleman, no hidden fees.', icon: 'ph:currency-dollar', iconBg: 'bg-brand-pink', rotation: 'rotate-3' },
  { title: 'Integrations Ecosystem', description: 'Connect Shopify, Stripe, PayPal, Spotify, Instagram, TikTok, YouTube & 50+ more platforms seamlessly.', icon: 'ph:plugs', iconBg: 'bg-brand-yellow', rotation: '-rotate-6' },
]

const templates = [
  { title: 'Storefront', badge: 'Popular', badgeBg: 'bg-brand-green', gradient: 'bg-gradient-to-br from-brand-yellow to-brand-pink', icon: 'ph:storefront', decoClass: 'absolute -top-6 -right-6 w-24 h-24 bg-black rotate-12', description: 'Perfect for affiliates and e-commerce. Showcase products with a visual grid layout.' },
  { title: 'Minimalist', badge: 'Clean', badgeBg: 'bg-brand-yellow', gradient: 'bg-gradient-to-br from-brand-blue to-brand-green', icon: 'ph:user-circle', decoClass: 'absolute -bottom-6 -left-6 w-24 h-24 bg-black -rotate-12', description: 'Clean and minimal design for creators who want their content to speak first.' },
  { title: 'Ultimate', badge: 'Pro', badgeBg: 'bg-brand-pink text-white', gradient: 'bg-gradient-to-br from-brand-pink to-brand-blue', icon: 'ph:megaphone', decoClass: 'absolute top-6 -right-8 w-16 h-16 bg-black rounded-full', description: 'Full-featured layout with video, products, social feeds, and advanced blocks.' },
]

const pricing = [
  {
    name: 'Free', price: '$0', period: 'Forever free', badge: '', badgeBg: '',
    cta: 'Get Started', ctaClass: 'bg-black text-white',
    features: [
      { text: 'Unlimited links', included: true },
      { text: 'Basic analytics', included: true },
      { text: '1 theme', included: true },
      { text: 'Linkto branding', included: true },
      { text: 'Custom domain', included: false },
    ],
  },
  {
    name: 'Starter', price: '$5', period: 'Per month', badge: 'POPULAR', badgeBg: 'bg-brand-yellow',
    cta: 'Start Free Trial', ctaClass: 'bg-brand-pink text-black',
    features: [
      { text: 'Everything in Free', included: true },
      { text: 'Advanced analytics', included: true },
      { text: '10 themes', included: true },
      { text: 'Link scheduling', included: true },
      { text: 'Remove Linkto branding', included: true },
    ],
  },
  {
    name: 'Pro', price: '$12', period: 'Per month', badge: '', badgeBg: '',
    cta: 'Start Free Trial', ctaClass: 'bg-brand-yellow text-black',
    features: [
      { text: 'Everything in Starter', included: true },
      { text: 'Custom domain', included: true },
      { text: 'Priority support', included: true },
      { text: 'Monetization tools', included: true },
      { text: 'SEO controls', included: true },
    ],
  },
  {
    name: 'Premium', price: '$24', period: 'Per month', badge: 'BEST VALUE', badgeBg: 'bg-black text-white',
    cta: 'Start Free Trial', ctaClass: 'bg-brand-green text-black',
    features: [
      { text: 'Everything in Pro', included: true },
      { text: 'Unlimited themes', included: true },
      { text: 'Team collaboration', included: true },
      { text: 'Marketing integrations', included: true },
      { text: 'Dedicated account manager', included: true },
    ],
  },
]

const reviews = [
  { name: 'Sarah Chen', role: 'Tech YouTuber · 2.4M subs', avatarBg: 'bg-brand-yellow', text: 'Linkto completely changed how I share my content. The affiliate hub alone increased my commission by 40%. It\'s like having a full e-commerce storefront in one link.' },
  { name: 'Marcus Rivera', role: 'Affiliate Marketer · $500k/yr', avatarBg: 'bg-brand-pink', text: 'The analytics alone are worth it. I can see exactly which products are converting and optimize my affiliate strategy. The Neo Brutalist design is just a bonus that makes me stand out.' },
  { name: 'Emma Watson', role: 'Fashion Influencer · 1.2M followers', avatarBg: 'bg-brand-blue', text: 'I\'ve tried every link-in-bio platform out there. Linkto is the only one that combines beautiful design with actual monetization tools. My followers actually buy through my links now.' },
  { name: 'Alex Thompson', role: 'Digital Creator · Newsletter writer', avatarBg: 'bg-brand-green', text: 'The scheduling feature is a game-changer. I set up my links for the entire month and they automatically rotate. My engagement has never been higher!' },
  { name: 'Priya Sharma', role: 'Small Business Owner', avatarBg: 'bg-brand-yellow', text: 'I run a small business and Linkto has become our primary sales channel. The product grid layout makes us look like a real online store. Best decision we ever made.' },
  { name: 'David Kim', role: 'Musician · Spotify Viral', avatarBg: 'bg-brand-blue', text: 'The custom domain feature with Neo Brutalism themes makes my link-in-bio feel like a real website. People actually compliment my \'website\' — that\'s the power of Linkto.' },
]

useSeoMeta({
  title: 'Linkto — Everything you are. In one link.',
  ogTitle: 'Linkto — Everything you are. In one link.',
  description: 'Join 10+ million creators, affiliates, and brands building their online hub. One link to help you share everything you create.',
  ogDescription: 'Join 10+ million creators, affiliates, and brands building their online hub. One link to help you share everything you create.',
})
</script>
