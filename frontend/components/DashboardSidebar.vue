<template>
  <aside class="w-64 bg-white border-r border-gray-200 flex-shrink-0 hidden md:flex flex-col justify-between shadow-sm z-20">
    <div class="flex flex-col h-full overflow-y-auto no-scrollbar">
      <!-- Logo -->
      <div class="h-20 flex items-center px-6 border-b border-gray-100 cursor-pointer sticky top-0 bg-white">
        <NuxtLink to="/dashboard" class="flex items-center">
          <div class="w-8 h-8 bg-black rounded-xl flex items-center justify-center mr-3 hover:scale-105 transition-transform">
            <Icon name="ph:link" class="text-white text-xl" />
          </div>
          <span class="font-black text-2xl tracking-tight">Linkto.</span>
        </NuxtLink>
      </div>

      <!-- Nav Links -->
      <nav class="p-4 space-y-1 flex-1">
        <p class="px-4 text-xs font-bold text-gray-400 uppercase tracking-wider mb-2 mt-2">Content</p>
        <NuxtLink to="/dashboard" class="flex items-center gap-3 px-4 py-3 rounded-xl"
          :class="route.path === '/dashboard' ? 'bg-gray-100 text-black font-semibold' : 'text-gray-600 font-medium hover:bg-gray-50 hover:text-black transition-colors'">
          <Icon name="ph:list-dashes" class="text-xl" /> Links
        </NuxtLink>

        <p class="px-4 text-xs font-bold text-gray-400 uppercase tracking-wider mb-2 mt-6">Design & Data</p>
        <NuxtLink to="/dashboard/settings" class="flex items-center gap-3 px-4 py-3 rounded-xl"
          :class="route.path === '/dashboard/settings' ? 'bg-gray-100 text-black font-semibold' : 'text-gray-600 font-medium hover:bg-gray-50 hover:text-black transition-colors'">
          <Icon name="ph:paint-brush" class="text-xl" /> Appearance
        </NuxtLink>
        <NuxtLink to="/dashboard/preview" class="flex items-center gap-3 px-4 py-3 rounded-xl"
          :class="route.path === '/dashboard/preview' ? 'bg-gray-100 text-black font-semibold' : 'text-gray-600 font-medium hover:bg-gray-50 hover:text-black transition-colors'">
          <Icon name="ph:eye" class="text-xl" /> Preview
        </NuxtLink>
        <NuxtLink to="/dashboard/analytics" class="flex items-center gap-3 px-4 py-3 rounded-xl"
          :class="route.path === '/dashboard/analytics' ? 'bg-gray-100 text-black font-semibold' : 'text-gray-600 font-medium hover:bg-gray-50 hover:text-black transition-colors'">
          <Icon name="ph:chart-line-up" class="text-xl" /> Analytics
        </NuxtLink>

        <p class="px-4 text-xs font-bold text-gray-400 uppercase tracking-wider mb-2 mt-6">Account</p>
        <NuxtLink to="/dashboard/settings" class="flex items-center gap-3 px-4 py-3 rounded-xl"
          :class="route.path === '/dashboard/settings' && route.query.tab === 'account' ? 'bg-gray-100 text-black font-semibold' : 'text-gray-600 font-medium hover:bg-gray-50 hover:text-black transition-colors'">
          <Icon name="ph:gear" class="text-xl" /> Settings
        </NuxtLink>

        <hr class="my-4 border-gray-100">

        <NuxtLink to="/" class="flex items-center gap-3 px-4 py-3 text-gray-600 font-medium rounded-xl hover:bg-gray-50 hover:text-black transition-colors">
          <Icon name="ph:eye" class="text-xl" /> View Public Page
        </NuxtLink>
        <button @click="handleLogout" class="w-full flex items-center gap-3 px-4 py-3 text-gray-600 font-medium rounded-xl hover:bg-red-50 hover:text-red-600 transition-colors">
          <Icon name="ph:sign-out" class="text-xl" /> Logout
        </button>
      </nav>
    </div>

    <!-- User Profile (Bottom) -->
    <div class="p-4 border-t border-gray-100 bg-white sticky bottom-0">
      <div class="flex items-center gap-3 px-4 py-2 hover:bg-gray-50 rounded-xl cursor-pointer border border-transparent hover:border-gray-200 transition-all">
        <div class="w-10 h-10 bg-gray-200 rounded-full overflow-hidden">
          <img v-if="user?.profile?.avatar_url" :src="user.profile.avatar_url" alt="Avatar" class="w-full h-full object-cover">
          <div v-else class="w-full h-full flex items-center justify-center bg-black text-white font-bold text-sm">
            {{ user?.username?.charAt(0)?.toUpperCase() || 'U' }}
          </div>
        </div>
        <div class="flex-1 min-w-0">
          <p class="font-semibold text-sm truncate text-black">{{ user?.profile?.full_name || user?.username || 'User' }}</p>
          <p class="text-xs text-gray-500 truncate">linkto.com/{{ user?.username }}</p>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
const route = useRoute()
const { user, logout } = useAuth()

async function handleLogout() {
  await logout()
}
</script>
