<template>
  <div class="h-screen flex overflow-hidden bg-[#F9FAFB] selection:bg-brand-pink selection:text-white">
    <!-- Sidebar -->
    <DashboardSidebar />

    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-full overflow-hidden">
      <!-- Mobile Header -->
      <header class="md:hidden bg-white h-16 border-b border-gray-200 flex items-center justify-between px-4 z-20">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-black rounded-xl flex items-center justify-center">
            <Icon name="ph:link" class="text-white text-lg font-bold" />
          </div>
          <span class="font-black text-xl">Linkto.</span>
        </div>
        <button @click="mobileMenuOpen = !mobileMenuOpen" class="text-gray-800 p-2 hover:bg-gray-100 rounded-lg">
          <Icon :name="mobileMenuOpen ? 'ph:x' : 'ph:list'" class="text-2xl" />
        </button>
      </header>

      <!-- Mobile Menu Overlay -->
      <div v-if="mobileMenuOpen" class="md:hidden fixed inset-0 z-30 bg-black/20" @click="mobileMenuOpen = false" />

      <div class="flex-1 overflow-y-auto p-4 sm:p-8 flex justify-center w-full">
        <div class="w-full max-w-3xl space-y-6 pb-20">
          <slot />
        </div>
      </div>
    </main>

    <!-- Live Preview (Desktop) -->
    <aside class="hidden lg:flex w-[420px] border-l border-gray-200 bg-white flex-col items-center justify-start p-8 z-10 shadow-[-4px_0_24px_rgba(0,0,0,0.02)] overflow-y-auto">
      <DashboardPreview />
    </aside>
  </div>
</template>

<script setup lang="ts">
const mobileMenuOpen = ref(false)
</script>
