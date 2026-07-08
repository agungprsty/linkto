<template>
  <div class="min-h-screen flex justify-center items-start sm:py-10" :style="{ backgroundColor: themeColors.background }">
    <!-- Main Container -->
    <main class="w-full sm:max-w-[480px] bg-noise min-h-screen sm:min-h-0 sm:rounded-[40px] shadow-2xl relative overflow-hidden flex flex-col items-center pb-8">

      <!-- Loading -->
      <div v-if="loading" class="py-20 text-center">
        <Icon name="ph:spinner" class="animate-spin text-4xl text-gray-400 mx-auto mb-4" />
        <p class="font-semibold text-gray-500">Loading...</p>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="py-20 text-center px-4">
        <div class="w-20 h-20 bg-gray-200 rounded-full flex items-center justify-center mx-auto mb-4">
          <Icon name="ph:user-x" class="text-3xl text-gray-400" />
        </div>
        <h2 class="text-2xl font-black mb-2">User not found</h2>
        <p class="font-semibold text-gray-500 mb-6">The page you're looking for doesn't exist.</p>
        <NuxtLink to="/" class="bg-black text-white font-bold px-8 py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full inline-flex items-center gap-2">
          <Icon name="ph:arrow-left" /> Go Home
        </NuxtLink>
      </div>

      <!-- Content -->
      <template v-else-if="profile">
        <!-- Header -->
        <header class="w-full flex justify-between items-center px-5 py-4">
          <NuxtLink v-if="backUrl" :to="backUrl"
            class="w-10 h-10 flex items-center justify-center rounded-full hover:bg-black/5 transition-colors" aria-label="Back">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="15 18 9 12 15 6" />
            </svg>
          </NuxtLink>
          <button v-else @click="showMenu = !showMenu" class="w-10 h-10 flex items-center justify-center rounded-full hover:bg-black/5 transition-colors">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0L13.5 8.5L22 10L14.5 13.5L16 22L12 16L8 22L9.5 13.5L2 10L10.5 8.5L12 0Z" /></svg>
          </button>
          <div class="flex items-center gap-3">
            <button @click="shareProfile"
              class="w-10 h-10 flex items-center justify-center rounded-full hover:bg-black/5 transition-colors" aria-label="Share profile">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8" /><polyline points="16 6 12 2 8 6" /><line x1="12" y1="2" x2="12" y2="15" />
              </svg>
            </button>
          </div>
        </header>

        <!-- Profile -->
        <div class="flex flex-col items-center mt-2 mb-6 px-4">
          <div class="relative">
            <div class="w-[96px] h-[96px] rounded-full bg-gray-200 overflow-hidden flex items-center justify-center">
              <img v-if="profile.avatar_url" :src="profile.avatar_url" :alt="username" class="w-full h-full object-cover">
              <div v-else class="w-full h-full flex items-center justify-center bg-black text-white font-bold text-2xl">
                {{ username?.charAt(0)?.toUpperCase() || '?' }}
              </div>
            </div>
          </div>
          <h1 class="text-[22px] font-bold text-black mt-4 tracking-tight">{{ profile.full_name || '@' + username }}</h1>
          <p v-if="profile.bio" class="text-sm font-medium text-gray-500 text-center mt-1 max-w-[250px]">{{ profile.bio }}</p>
        </div>

        <!-- Links -->
        <div class="w-full px-4 space-y-3 relative">
          <template v-for="link in links" :key="link.id">
            <!-- Standard Link -->
            <a v-if="link.type === 'standard'"
              :href="link.url" target="_blank" rel="noopener noreferrer"
              @click="onLinkClick(link.id)"
              class="link-card w-full bg-white rounded-[28px] p-2 pr-4 flex items-center min-h-[64px] shadow-link group">
              <div class="w-12 h-12 rounded-xl bg-black flex-shrink-0 flex items-center justify-center">
                <Icon name="ph:link-simple" class="text-white text-xl" />
              </div>
              <div class="flex-1 text-center px-2">
                <span class="font-semibold text-[14px] text-black leading-tight">{{ link.title }}</span>
              </div>
              <div class="w-6 flex justify-end text-gray-300">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="12" cy="19" r="1.5"/></svg>
              </div>
            </a>

            <!-- Affiliate Product -->
            <a v-else
              :href="link.url" target="_blank" rel="noopener noreferrer nofollow"
              @click="onLinkClick(link.id)"
              class="link-card w-full bg-white rounded-[28px] p-2 pr-4 flex items-center min-h-[64px] shadow-link group">
              <div class="w-12 h-12 rounded-xl bg-gray-100 flex-shrink-0 flex items-center justify-center overflow-hidden">
                <img v-if="link.image_url" :src="link.image_url" :alt="link.title" class="w-full h-full object-cover">
                <Icon v-else name="ph:shopping-bag" class="text-gray-400 text-xl" />
              </div>
              <div class="flex-1 text-center px-2">
                <span class="font-semibold text-[14px] text-black leading-tight">{{ link.title }}</span>
              </div>
              <div class="w-6 flex justify-end text-gray-300">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="12" cy="19" r="1.5"/></svg>
              </div>
            </a>
          </template>
        </div>

        <!-- Footer -->
        <div class="mt-auto w-full flex flex-col items-center pb-4 px-4" :class="links.length < 2 ? 'mt-10' : 'mt-16'">
          <a v-if="showJoinLink" :href="joinUrl" target="_blank" rel="noopener noreferrer"
            class="bg-white text-black font-bold text-[15px] py-4 px-8 rounded-full shadow-join hover:scale-105 transition-transform mb-8">
            Join {{ username }} on Linkto
          </a>
          <div class="flex flex-wrap justify-center items-center gap-x-2 gap-y-1 text-[11px] text-gray-500 font-medium">
            <NuxtLink to="/privacy" class="hover:underline">Privacy</NuxtLink>
            <span>•</span>
            <NuxtLink to="/terms" class="hover:underline">Terms</NuxtLink>
            <span>•</span>
            <span>Powered by <NuxtLink to="/" class="font-bold hover:underline">Linkto</NuxtLink></span>
          </div>
        </div>
      </template>
    </main>

    <!-- Share FAB -->
    <button @click="shareProfile"
      class="fixed bottom-6 right-6 w-14 h-14 bg-black text-white rounded-2xl shadow-float flex items-center justify-center hover:scale-105 active:scale-95 transition-transform md:hidden z-50" aria-label="Share">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8" /><polyline points="16 6 12 2 8 6" /><line x1="12" y1="2" x2="12" y2="15" />
      </svg>
    </button>
  </div>
</template>

<script setup lang="ts">
import type { Link, UserProfile, UserTheme } from '~/types'

interface Props {
  username: string
  profile: UserProfile | null
  links: Link[]
  theme?: UserTheme | null
  loading?: boolean
  error?: string | null
  showJoinLink?: boolean
  joinUrl?: string
  backUrl?: string
}

const props = withDefaults(defineProps<Props>(), {
  theme: null,
  loading: false,
  error: null,
  showJoinLink: true,
  joinUrl: '/auth/register',
  backUrl: '',
})

const emit = defineEmits<{
  click: [linkId: string]
}>()

const showMenu = ref(false)

// Theme colors
const themeColors = computed(() => ({
  background: props.theme?.background_color || '#B4B4B4',
}))

// Share
const shareData = computed(() => ({
  title: `${props.username || 'Linkto'} on Linkto`,
  text: `Check out ${props.username || 'this profile'} on Linkto!`,
  url: window.location.href,
}))

async function shareProfile() {
  if (navigator.share) {
    try {
      await navigator.share(shareData.value)
    } catch {
      fallbackCopyLink()
    }
  } else {
    fallbackCopyLink()
  }
}

function fallbackCopyLink() {
  navigator.clipboard.writeText(window.location.href).then(() => {
    showToast('Link copied to clipboard!')
  }).catch(() => {
    prompt('Copy this link:', window.location.href)
  })
}

function showToast(msg: string) {
  const existing = document.querySelector('.toast-msg')
  if (existing) existing.remove()
  const toast = document.createElement('div')
  toast.className = 'toast-msg fixed bottom-24 left-1/2 -translate-x-1/2 bg-black text-white text-sm font-medium px-5 py-3 rounded-full shadow-float z-50'
  toast.textContent = msg
  document.body.appendChild(toast)
  setTimeout(() => {
    toast.style.opacity = '0'
    toast.style.transition = 'opacity 0.3s'
    setTimeout(() => toast.remove(), 300)
  }, 2000)
}

function onLinkClick(linkId: string) {
  emit('click', linkId)
}
</script>

<style scoped>
/* Subtle Noise/Grain Texture */
.bg-noise {
  background-color: #FAFAFA;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.04'/%3E%3C/svg%3E");
}

.link-card {
  transition: transform 0.15s cubic-bezier(0, 0, 0.2, 1);
}
.link-card:hover {
  transform: scale(1.02);
}

.shadow-link {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04), 0 4px 16px rgba(0, 0, 0, 0.02);
}

.shadow-float {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.shadow-join {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}
</style>
