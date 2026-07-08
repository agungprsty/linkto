<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden bg-brand-bg border-b-4 border-black">
      <div class="hidden md:block absolute top-10 left-10 w-48 h-48 bg-brand-yellow border-4 border-black rounded-full -z-0 float-slow" />
      <div class="hidden md:block absolute bottom-10 right-10 w-36 h-36 bg-brand-pink border-4 border-black -z-0 rotate-12" />
      <div class="md:hidden absolute -top-6 -right-6 w-24 h-24 bg-brand-pink border-4 border-black -z-0 rotate-12 opacity-30" />
      <div class="md:hidden absolute -bottom-4 -left-4 w-16 h-16 bg-brand-yellow border-4 border-black rounded-full -z-0 opacity-30" />
      <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24 text-center relative z-10">
        <h1 class="text-4xl sm:text-5xl md:text-7xl font-black leading-[1.1]">
          We're on a mission to<br>
          <span class="bg-brand-yellow px-4 border-4 border-black shadow-brutal inline-block mt-3 md:mt-4 -rotate-1 hover:rotate-1 transition-transform">empower every creator.</span>
        </h1>
        <p class="text-base sm:text-lg md:text-xl font-semibold text-gray-700 mt-6 md:mt-8 max-w-3xl mx-auto">Linkto was born from a simple idea: everyone deserves a beautiful, powerful link-in-bio that actually helps them grow. No coding. No hassle. Just pure conversion.</p>
      </div>
    </section>

    <!-- Story -->
    <section class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-20">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div class="bg-white border-4 border-black shadow-brutal p-8 -rotate-1 hover:rotate-0 transition-transform">
          <h2 class="text-3xl font-black mb-4">Our Story</h2>
          <p class="font-semibold text-gray-700 leading-relaxed mb-4">Founded in 2026, Linkto started as a side project by a group of creators who were frustrated with the limited options for link-in-bio platforms. We wanted something that didn't just look good, but actually helped creators make money.</p>
          <p class="font-semibold text-gray-700 leading-relaxed">Today, Linkto powers over 10 million creators worldwide — from solo influencers to Fortune 500 companies. We've built the most customizable, conversion-optimized link-in-bio platform on the market.</p>
        </div>
        <div class="bg-brand-blue border-4 border-black shadow-brutal-lg p-8 rotate-1 hover:rotate-0 transition-transform">
          <div class="grid grid-cols-2 gap-6 text-center">
            <div><p class="text-4xl font-black">10M+</p><p class="font-bold text-sm">Creators</p></div>
            <div><p class="text-4xl font-black">195+</p><p class="font-bold text-sm">Countries</p></div>
            <div><p class="text-4xl font-black">500M+</p><p class="font-bold text-sm">Monthly Views</p></div>
            <div><p class="text-4xl font-black">$50M+</p><p class="font-bold text-sm">Affiliate Sales</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Values -->
    <section class="bg-black border-y-4 border-black py-12 md:py-20">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-4xl md:text-5xl font-black text-white mb-12">What we stand for</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div v-for="value in values" :key="value.title"
            class="bg-white border-4 border-black shadow-brutal p-8 hover:-translate-y-2 transition-all">
            <div :class="`w-14 h-14 ${value.iconBg} border-4 border-black rounded-full flex items-center justify-center mx-auto mb-5 ${value.rotation}`">
              <Icon :name="value.icon" class="text-3xl font-bold" />
            </div>
            <h3 class="font-black text-xl mb-3">{{ value.title }}</h3>
            <p class="font-semibold text-gray-600">{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Team -->
    <section class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-20">
      <div class="text-center mb-12">
        <h2 class="text-4xl md:text-5xl font-black inline-block bg-white border-4 border-black px-6 py-3 shadow-brutal rotate-1 hover:rotate-0 transition-transform">Meet the Team</h2>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div v-for="member in team" :key="member.name"
          class="bg-white border-4 border-black shadow-brutal-sm p-6 text-center hover:shadow-brutal hover:-translate-y-1 transition-all">
          <div :class="`w-20 h-20 mx-auto rounded-full border-4 border-black ${member.bg} flex items-center justify-center mb-4`">
            <span class="font-black text-2xl">{{ member.initials }}</span>
          </div>
          <h3 class="font-black">{{ member.name }}</h3>
          <p class="text-sm font-bold text-gray-500">{{ member.role }}</p>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-brand-yellow border-y-4 border-black py-12 md:py-20 text-center">
      <div class="max-w-3xl mx-auto px-4">
        <h2 class="text-4xl md:text-5xl font-black">Join 10M+ creators</h2>
        <p class="text-xl font-bold text-black/70 mt-4 mb-8">Start your Linkto journey today. It's free.</p>
        <NuxtLink to="/auth/register"
          class="inline-flex items-center gap-2 bg-black text-white font-black text-xl px-10 py-5 border-4 border-black shadow-brutal hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
          Create Your Linkto <Icon name="ph:arrow-right" class="font-bold" />
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const values = [
  { title: 'Creator First', description: 'Every feature we build starts with a creator\'s need. We put our users before profits.', icon: 'ph:hand-heart', iconBg: 'bg-brand-pink', rotation: '-rotate-6' },
  { title: 'Radical Simplicity', description: 'Powerful tools don\'t have to be complicated. We make the complex simple.', icon: 'ph:lightning', iconBg: 'bg-brand-yellow', rotation: 'rotate-3' },
  { title: 'Open & Accessible', description: 'Linkto is free to start. Everyone deserves a beautiful link-in-bio, regardless of budget.', icon: 'ph:globe', iconBg: 'bg-brand-green', rotation: '-rotate-3' },
]

const team = [
  { name: 'Agung Prastyo', initials: 'AP', role: 'Founder & CEO', bg: 'bg-brand-yellow' },
  { name: 'Sarah Chen', initials: 'SC', role: 'CTO', bg: 'bg-brand-pink' },
  { name: 'Marcus Rivera', initials: 'MR', role: 'Head of Product', bg: 'bg-brand-blue' },
  { name: 'Priya Sharma', initials: 'PS', role: 'Head of Design', bg: 'bg-brand-green' },
]

useSeoMeta({ title: 'About Us — Linkto' })
</script>
