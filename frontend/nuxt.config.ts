// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  // Modules
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
    'nuxt-icon',
    '@vueuse/nuxt',
    '@nuxtjs/color-mode',
  ],

  // App config
  app: {
    head: {
      title: 'Linkto — Everything you are. In one link.',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Join 10+ million creators, affiliates, and brands building their online hub. One link to help you share everything you create.' },
        { name: 'theme-color', content: '#F3F3F1' },
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: 'anonymous' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap' },
      ],
      script: [
        { src: 'https://unpkg.com/@phosphor-icons/web', tagPosition: 'head' },
      ],
    },
  },

  // Runtime config for API URL
  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.NUXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1',
    },
  },

  // Tailwind CSS
  tailwindcss: {
    configPath: '~/tailwind.config.ts',
    exposeConfig: true,
  },

  // Color mode
  colorMode: {
    classSuffix: '',
    preference: 'light',
    fallback: 'light',
  },

  // Pinia
  pinia: {
    storesDirs: ['~/stores/**'],
  },

  // Typescript
  typescript: {
    strict: true,
    typeCheck: false,
  },

  // CSS
  css: ['~/assets/css/main.css'],

  // Route rules
  routeRules: {
    // Dashboard pages are SPA (no SSR needed)
    '/dashboard/**': { ssr: false },
    // Public bio pages use SSR for SEO
    '/**': { ssr: true },
  },

  nitro: {
    preset: 'node-server',
  },
})
