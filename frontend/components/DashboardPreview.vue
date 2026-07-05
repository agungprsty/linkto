<template>
  <div class="w-full max-w-[300px]">
    <div class="flex items-center justify-between w-full mb-6">
      <span class="text-sm font-bold text-gray-400 uppercase tracking-widest">Live Preview</span>
      <a v-if="authStore.username" :href="`/${authStore.username}`" target="_blank"
        class="text-sm font-bold text-brand-blue flex items-center gap-1 hover:underline bg-blue-50 px-3 py-1.5 rounded-full">
        <Icon name="ph:arrow-square-out" /> linkto.com/{{ authStore.username }}
      </a>
    </div>

    <!-- Phone Frame -->
    <div class="relative w-[300px] h-[620px] bg-black rounded-[3rem] shadow-[0_20px_50px_rgba(0,0,0,0.15)] p-2">
      <div class="w-full h-full bg-[#F3F4F6] rounded-[2.5rem] overflow-hidden relative border border-gray-800">
        <!-- Dynamic Island -->
        <div class="absolute top-2 left-1/2 -translate-x-1/2 w-24 h-6 bg-black rounded-full z-30" />

        <!-- Screen Content -->
        <div class="w-full h-full overflow-y-auto no-scrollbar pb-10 relative z-10">
          <!-- Profile Header -->
          <div class="pt-14 pb-6 flex flex-col items-center px-4">
            <div class="w-24 h-24 bg-gray-200 rounded-full overflow-hidden shadow-sm mb-4 border-2 border-white">
              <img v-if="authStore.user?.profile?.avatar_url" :src="authStore.user.profile.avatar_url" alt="Avatar" class="w-full h-full object-cover">
              <div v-else class="w-full h-full flex items-center justify-center bg-black text-white font-bold text-2xl">
                {{ authStore.user?.username?.charAt(0)?.toUpperCase() || '?' }}
              </div>
            </div>
            <h2 class="font-black text-xl text-gray-900 tracking-tight">@{{ authStore.user?.username || 'username' }}</h2>
            <p v-if="authStore.user?.profile?.bio" class="text-sm font-medium text-gray-600 text-center mt-2 max-w-[200px] leading-relaxed">
              {{ authStore.user.profile.bio }}
            </p>
          </div>

          <!-- Links -->
          <div class="px-5 space-y-3">
            <div v-for="link in linksStore.sortedLinks.filter(l => l.is_active)" :key="link.id">
              <!-- Standard Link -->
              <a v-if="link.type === 'standard'" :href="link.url" target="_blank"
                class="block w-full bg-white border border-gray-100 rounded-2xl p-4 text-center text-sm font-bold text-gray-800 shadow-[0_2px_8px_rgba(0,0,0,0.04)] hover:scale-[1.02] transition-transform">
                {{ link.title }}
              </a>
              <!-- Affiliate Product -->
              <div v-else class="bg-white border border-gray-100 rounded-2xl p-3 shadow-[0_2px_8px_rgba(0,0,0,0.04)] hover:scale-[1.02] transition-transform flex flex-col">
                <div class="w-full aspect-square bg-gray-100 rounded-xl overflow-hidden mb-2">
                  <img v-if="link.image_url" :src="link.image_url" :alt="link.title" class="w-full h-full object-cover">
                  <div v-else class="w-full h-full flex items-center justify-center text-gray-400">
                    <Icon name="ph:image" class="text-3xl" />
                  </div>
                </div>
                <p class="text-[11px] font-bold text-gray-800 line-clamp-2 leading-tight">{{ link.title }}</p>
              </div>
            </div>
          </div>

          <div class="mt-10 text-center pb-6">
            <span class="text-[10px] font-black tracking-widest uppercase text-gray-400">Powered by Linkto</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth'
import { useLinksStore } from '~/stores/links'

const authStore = useAuthStore()
const linksStore = useLinksStore()
</script>
