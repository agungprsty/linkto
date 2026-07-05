<template>
  <div>
    <div class="flex items-center justify-between mb-8">
      <h1 class="text-3xl font-black">Settings</h1>
    </div>

    <!-- Error -->
    <div v-if="error" class="bg-red-50 border border-red-200 rounded-2xl p-4 mb-6">
      <p class="font-semibold text-red-700">{{ error }}</p>
    </div>

    <!-- Success -->
    <div v-if="saved" class="bg-green-50 border border-green-200 rounded-2xl p-4 mb-6">
      <p class="font-semibold text-green-700 flex items-center gap-2">
        <Icon name="ph:check-circle" class="text-xl" /> Settings saved successfully!
      </p>
    </div>

    <!-- Tabs -->
    <div class="flex gap-1 mb-8 bg-gray-100 p-1 rounded-xl">
      <button @click="activeTab = 'profile'"
        class="flex-1 py-3 px-4 rounded-lg font-bold text-sm transition-all"
        :class="activeTab === 'profile' ? 'bg-white shadow-sm text-black' : 'text-gray-500 hover:text-black'">
        <Icon name="ph:user" class="inline mr-1" /> Profile
      </button>
      <button @click="activeTab = 'theme'"
        class="flex-1 py-3 px-4 rounded-lg font-bold text-sm transition-all"
        :class="activeTab === 'theme' ? 'bg-white shadow-sm text-black' : 'text-gray-500 hover:text-black'">
        <Icon name="ph:paint-brush" class="inline mr-1" /> Appearance
      </button>
    </div>

    <!-- Profile Tab -->
    <div v-if="activeTab === 'profile'" class="space-y-6">
      <div class="bg-white rounded-2xl border border-gray-200 p-6 space-y-5">
        <h2 class="font-black text-xl">Profile Information</h2>

        <div>
          <label class="block font-bold text-sm mb-2">Username</label>
          <div class="flex border-4 border-black shadow-brutal-sm">
            <span class="flex items-center pl-3 pr-2 text-sm font-bold text-gray-400 pointer-events-none bg-gray-50 border-r-4 border-black whitespace-nowrap">linkto.com/</span>
            <input v-model="profileForm.username" type="text" disabled
              class="flex-1 min-w-0 py-3 px-3 font-semibold bg-gray-50 text-gray-500 border-0 outline-none">
          </div>
        </div>

        <div>
          <label class="block font-bold text-sm mb-2">Full Name</label>
          <input v-model="profileForm.full_name" type="text" placeholder="Your name"
            class="w-full border-4 border-black py-3.5 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
        </div>

        <div>
          <label class="block font-bold text-sm mb-2">Bio</label>
          <textarea v-model="profileForm.bio" rows="3" placeholder="Tell your story..."
            class="w-full border-4 border-black py-3.5 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all resize-none" />
        </div>

        <div>
          <label class="block font-bold text-sm mb-2">Avatar URL</label>
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 bg-gray-100 rounded-full overflow-hidden border-2 border-black flex-shrink-0">
              <img v-if="profileForm.avatar_url" :src="profileForm.avatar_url" alt="Avatar" class="w-full h-full object-cover">
              <div v-else class="w-full h-full flex items-center justify-center text-gray-400">
                <Icon name="ph:user" class="text-2xl" />
              </div>
            </div>
            <input v-model="profileForm.avatar_url" type="url" placeholder="https://..."
              class="flex-1 border-4 border-black py-3 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
          </div>
        </div>

        <button @click="saveProfile"
          class="bg-black text-white font-bold px-8 py-3.5 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
          Save Profile
        </button>
      </div>
    </div>

    <!-- Theme Tab -->
    <div v-if="activeTab === 'theme'" class="space-y-6">
      <div class="bg-white rounded-2xl border border-gray-200 p-6 space-y-5">
        <h2 class="font-black text-xl">Theme Customization</h2>

        <div>
          <label class="block font-bold text-sm mb-2">Background Color</label>
          <div class="flex items-center gap-3">
            <input v-model="themeForm.background_color" type="color" class="w-16 h-16 border-4 border-black cursor-pointer">
            <input v-model="themeForm.background_color" type="text" placeholder="#FFFFFF"
              class="flex-1 border-4 border-black py-3 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
          </div>
        </div>

        <div>
          <label class="block font-bold text-sm mb-2">Button Color</label>
          <div class="flex items-center gap-3">
            <input v-model="themeForm.button_color" type="color" class="w-16 h-16 border-4 border-black cursor-pointer">
            <input v-model="themeForm.button_color" type="text" placeholder="#000000"
              class="flex-1 border-4 border-black py-3 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
          </div>
        </div>

        <div>
          <label class="block font-bold text-sm mb-2">Button Style</label>
          <div class="flex gap-3">
            <button @click="themeForm.button_style = 'rounded'"
              class="flex-1 py-3 px-4 border-4 font-bold transition-all"
              :class="themeForm.button_style === 'rounded' ? 'bg-black text-white border-black' : 'bg-white text-black border-black hover:bg-gray-50'">
              Rounded
            </button>
            <button @click="themeForm.button_style = 'pill'"
              class="flex-1 py-3 px-4 border-4 font-bold transition-all rounded-full"
              :class="themeForm.button_style === 'pill' ? 'bg-black text-white border-black' : 'bg-white text-black border-black hover:bg-gray-50'">
              Pill
            </button>
            <button @click="themeForm.button_style = 'soft'"
              class="flex-1 py-3 px-4 border-4 font-bold transition-all"
              :class="themeForm.button_style === 'soft' ? 'bg-black text-white border-black' : 'bg-white text-black border-black hover:bg-gray-50'">
              Soft
            </button>
          </div>
        </div>

        <div>
          <label class="block font-bold text-sm mb-2">Font Family</label>
          <select v-model="themeForm.font_family"
            class="w-full border-4 border-black py-3.5 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
            <option value="Inter">Inter</option>
            <option value="Arial">Arial</option>
            <option value="Georgia">Georgia</option>
            <option value="system-ui">System UI</option>
          </select>
        </div>

        <button @click="saveTheme"
          class="bg-black text-white font-bold px-8 py-3.5 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
          Save Theme
        </button>
      </div>

      <!-- Theme Preview -->
      <div class="bg-white rounded-2xl border border-gray-200 p-6">
        <h3 class="font-black text-lg mb-4">Preview</h3>
        <div class="p-6 rounded-xl" :style="{ backgroundColor: themeForm.background_color }">
          <div class="text-center mb-4">
            <div class="w-16 h-16 rounded-full bg-gray-200 mx-auto mb-2" />
            <p class="font-bold" :style="{ fontFamily: themeForm.font_family }">Preview User</p>
          </div>
          <div class="space-y-2">
            <div class="p-4 text-center font-bold text-white" :style="{
              backgroundColor: themeForm.button_color,
              borderRadius: themeForm.button_style === 'pill' ? '9999px' : themeForm.button_style === 'soft' ? '12px' : '8px',
              fontFamily: themeForm.font_family,
            }">
              Sample Link Button
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth'
import { useThemeStore } from '~/stores/theme'

definePageMeta({
  layout: 'dashboard',
  middleware: 'auth',
})

const authStore = useAuthStore()
const themeStore = useThemeStore()
const { $api } = useNuxtApp()

const activeTab = ref('profile')
const error = ref('')
const saved = ref(false)

const profileForm = reactive({
  username: authStore.user?.username || '',
  full_name: authStore.user?.profile?.full_name || '',
  bio: authStore.user?.profile?.bio || '',
  avatar_url: authStore.user?.profile?.avatar_url || '',
})

const themeForm = reactive({
  background_color: themeStore.backgroundColor,
  button_color: themeStore.buttonColor,
  button_style: themeStore.buttonStyle,
  font_family: themeStore.fontFamily,
})

async function saveProfile() {
  error.value = ''
  saved.value = false
  try {
    const data = await $api('/user/profile', {
      method: 'PUT',
      body: {
        full_name: profileForm.full_name,
        bio: profileForm.bio,
        avatar_url: profileForm.avatar_url,
      },
    })
    if (authStore.user) {
      authStore.user.profile = data.profile
    }
    saved.value = true
    setTimeout(() => { saved.value = false }, 3000)
  } catch (e: any) {
    error.value = e?.data?.detail?.message || 'Failed to save profile'
  }
}

async function saveTheme() {
  error.value = ''
  saved.value = false
  try {
    const data = await $api('/user/profile', {
      method: 'PUT',
      body: {
        background_color: themeForm.background_color,
        button_color: themeForm.button_color,
        button_style: themeForm.button_style,
        font_family: themeForm.font_family,
      },
    })
    themeStore.setTheme(data.theme)
    if (authStore.user) {
      authStore.user.theme = data.theme
    }
    saved.value = true
    setTimeout(() => { saved.value = false }, 3000)
  } catch (e: any) {
    error.value = e?.data?.detail?.message || 'Failed to save theme'
  }
}
</script>
