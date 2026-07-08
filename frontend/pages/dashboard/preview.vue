<template>
  <BioPageContent
    :username="username"
    :profile="profile"
    :links="links"
    :theme="theme"
    :loading="false"
    :error="null"
    :show-join-link="false"
    back-url="/dashboard"
  />
</template>

<script setup lang="ts">
definePageMeta({
  layout: false,
  middleware: 'auth',
})

import { useAuthStore } from '~/stores/auth'
import { useLinksStore } from '~/stores/links'
import { useThemeStore } from '~/stores/theme'
import type { UserProfile, UserTheme } from '~/types'

const authStore = useAuthStore()
const linksStore = useLinksStore()
const themeStore = useThemeStore()

const username = computed(() => authStore.user?.username || 'username')

const profile = computed<UserProfile | null>(() => {
  if (!authStore.user?.profile) return null
  return {
    full_name: authStore.user.profile.full_name,
    bio: authStore.user.profile.bio,
    avatar_url: authStore.user.profile.avatar_url,
  }
})

const links = computed(() => linksStore.sortedLinks)

const theme = computed<UserTheme | null>(() => ({
  background_color: themeStore.backgroundColor,
  button_style: themeStore.buttonStyle,
  button_color: themeStore.buttonColor,
  font_family: themeStore.fontFamily,
}))

useSeoMeta({
  title: 'Preview — Linkto Dashboard',
})
</script>
