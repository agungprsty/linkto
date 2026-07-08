<template>
  <div>
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-12">
        <h1 class="text-5xl md:text-6xl font-black">Terms of Service</h1>
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
  { title: '1. Acceptance of Terms', content: 'By accessing or using Linkto ("the Service"), you agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use the Service.' },
  { title: '2. Description of Service', content: 'Linkto provides a platform that allows users to create a personalized landing page to consolidate and share links. The Service includes link management, analytics, and customization features.' },
  { title: '3. User Accounts', content: 'You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account. You must provide accurate and complete information when creating an account.' },
  { title: '4. Acceptable Use', content: 'You agree not to use the Service for any unlawful purpose or in violation of any applicable laws. You may not use the Service to distribute malware, spam, or harmful content.' },
  { title: '5. Intellectual Property', content: 'The Service and its original content, features, and functionality are owned by Linkto Inc. and are protected by international copyright, trademark, and other intellectual property laws.' },
  { title: '6. Limitation of Liability', content: 'Linkto Inc. shall not be liable for any indirect, incidental, special, consequential, or punitive damages arising out of your use of the Service.' },
  { title: '7. Changes to Terms', content: 'We reserve the right to modify these terms at any time. We will notify users of material changes via email or through the Service.' },
]

useSeoMeta({ title: 'Terms of Service — Linkto' })
</script>
