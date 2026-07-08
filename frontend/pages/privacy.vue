<template>
  <div>
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-12">
        <h1 class="text-5xl md:text-6xl font-black">Privacy Policy</h1>
        <p class="text-lg font-semibold text-gray-500 mt-4">Last updated: January 1, 2026</p>
      </div>

      <div class="bg-white border-4 border-black shadow-brutal p-8 md:p-12 space-y-8">
        <section v-for="section in sections" :key="section.title">
          <h2 class="text-2xl font-black mb-4">{{ section.title }}</h2>
          <p class="font-semibold text-gray-700 leading-relaxed" v-html="section.content" />
        </section>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const sections = [
  { title: '1. Information We Collect', content: 'We collect information you provide directly, such as your name, email address, and profile information. We also automatically collect information about your use of the Service, including page views, link clicks, and device information.' },
  { title: '2. How We Use Your Information', content: 'We use the information we collect to provide, maintain, and improve the Service, to communicate with you, and to develop new features.' },
  { title: '3. Information Sharing', content: 'We do not sell your personal information. We may share information with third-party service providers who assist us in operating the Service.' },
  { title: '4. Data Security', content: 'We implement industry-standard security measures to protect your information. However, no method of transmission over the Internet is 100% secure.' },
  { title: '5. Your Rights', content: 'You have the right to access, update, or delete your personal information. You can do this through your account settings or by contacting us.' },
  { title: '6. Cookies', content: 'We use cookies and similar tracking technologies to track activity on our Service and hold certain information. You can control cookie settings through your browser.' },
]

useSeoMeta({ title: 'Privacy Policy — Linkto' })
</script>
