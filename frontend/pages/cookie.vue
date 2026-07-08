<template>
  <div>
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-12">
        <h1 class="text-5xl md:text-6xl font-black">Cookie Policy</h1>
        <p class="text-lg font-semibold text-gray-500 mt-4">Last updated: January 1, 2026</p>
      </div>

      <div class="bg-white border-4 border-black shadow-brutal p-8 md:p-12 space-y-6">
        <section v-for="section in sections" :key="section.title">
          <h2 class="text-2xl font-black mb-3">{{ section.title }}</h2>
          <p class="font-semibold text-gray-700 leading-relaxed">{{ section.content }}</p>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const sections = [
  { title: 'What Are Cookies', content: 'Cookies are small text files stored on your device when you visit a website. They help websites remember your preferences and improve your browsing experience.' },
  { title: 'How We Use Cookies', content: 'We use cookies to: (1) Authenticate your account and keep you logged in, (2) Analyze how you use our Service to improve it, (3) Remember your preferences and settings.' },
  { title: 'Types of Cookies We Use', content: 'Essential cookies are required for the Service to function. Analytics cookies help us understand how users interact with our Service. Preference cookies remember your settings and choices.' },
  { title: 'Managing Cookies', content: 'You can control cookies through your browser settings. However, disabling certain cookies may affect the functionality of our Service.' },
  { title: 'Third-Party Cookies', content: 'We may use third-party services (such as Google Analytics) that set their own cookies. These are governed by the respective third-party privacy policies.' },
  { title: 'Contact Us', content: 'If you have questions about our Cookie Policy, please contact us at privacy@linkto.com.' },
]

useSeoMeta({ title: 'Cookie Policy — Linkto' })
</script>
