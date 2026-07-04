<template>
  <div>
    <main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-16">
        <div class="inline-block bg-black text-white px-4 py-1 rounded-full font-bold text-sm mb-6">🌍 COMMUNITY</div>
        <h1 class="text-5xl md:text-6xl font-black">Join Our Community</h1>
        <p class="text-lg font-semibold text-gray-500 mt-4 max-w-2xl mx-auto">Connect with 10M+ creators, share tips, and grow together.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
        <div class="bg-white border-4 border-black shadow-brutal p-8 hover:shadow-brutal-lg hover:-translate-y-2 transition-all text-center">
          <div class="w-20 h-20 bg-brand-pink border-4 border-black rounded-full flex items-center justify-center mx-auto mb-5 -rotate-6">
            <Icon name="ph:discord-logo" class="text-4xl font-bold" />
          </div>
          <h3 class="text-2xl font-black mb-3">Discord</h3>
          <p class="font-semibold text-gray-600 mb-6">Join our Discord server for real-time chat, support, and networking with fellow creators.</p>
          <a href="#" class="inline-flex items-center gap-2 bg-black text-white font-black px-8 py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
            Join Discord <Icon name="ph:arrow-right" class="font-bold" />
          </a>
        </div>

        <div class="bg-white border-4 border-black shadow-brutal p-8 hover:shadow-brutal-lg hover:-translate-y-2 transition-all text-center">
          <div class="w-20 h-20 bg-brand-blue border-4 border-black rounded-full flex items-center justify-center mx-auto mb-5 rotate-3">
            <Icon name="ph:users-three" class="text-4xl font-bold" />
          </div>
          <h3 class="text-2xl font-black mb-3">Events & Webinars</h3>
          <p class="font-semibold text-gray-600 mb-6">Attend monthly webinars, AMAs with successful creators, and virtual networking events.</p>
          <a href="#" class="inline-flex items-center gap-2 bg-black text-white font-black px-8 py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
            See Events <Icon name="ph:arrow-right" class="font-bold" />
          </a>
        </div>
      </div>

      <!-- Stats -->
      <div class="bg-black border-4 border-black py-12 text-center">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div><p class="text-4xl font-black text-white">10M+</p><p class="font-bold text-gray-400">Creators</p></div>
          <div><p class="text-4xl font-black text-white">50K+</p><p class="font-bold text-gray-400">Discord Members</p></div>
          <div><p class="text-4xl font-black text-white">500+</p><p class="font-bold text-gray-400">Events Hosted</p></div>
          <div><p class="text-4xl font-black text-white">195+</p><p class="font-bold text-gray-400">Countries</p></div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
useSeoMeta({ title: 'Community — Linkto' })
</script>
