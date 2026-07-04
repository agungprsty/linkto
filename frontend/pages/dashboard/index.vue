<template>
  <div>
    <!-- Alert Banner -->
    <div class="bg-blue-50 border border-blue-100 rounded-2xl p-4 flex gap-4 items-start">
      <div class="bg-blue-500 text-white p-2 rounded-full mt-0.5">
        <Icon name="ph:info" class="text-lg" />
      </div>
      <div>
        <h4 class="font-bold text-blue-900">New Feature: Smart Affiliate Scraper</h4>
        <p class="text-sm text-blue-800 mt-1">
          You can now paste a Shopee or Tokopedia link directly, and we will automatically fetch the image and title for your Storefront.
          <a href="#" class="font-bold underline">Try it now</a>.
        </p>
      </div>
    </div>

    <!-- Top Action Bar -->
    <div class="flex flex-col sm:flex-row gap-4 items-center justify-between sticky top-0 z-10 bg-[#F9FAFB] py-2">
      <button @click="openCreateModal('standard')"
        class="w-full sm:w-auto bg-black text-white px-8 py-3.5 rounded-full font-semibold hover:bg-gray-800 hover:scale-[1.02] transition-all shadow-md flex items-center justify-center gap-2">
        <Icon name="ph:plus-circle" class="text-xl" /> Add Link
      </button>
      <button @click="openCreateModal('affiliate_product')"
        class="w-full sm:w-auto bg-white border border-gray-200 text-gray-700 px-5 py-3.5 rounded-full font-semibold hover:bg-gray-50 hover:border-gray-300 transition-all shadow-sm text-sm flex items-center justify-center gap-2">
        <Icon name="ph:shopping-cart" class="text-lg" /> Add Product
      </button>
    </div>

    <!-- Error Alert -->
    <div v-if="linksStore.error" class="bg-red-50 border border-red-200 rounded-2xl p-4">
      <p class="font-semibold text-red-700 flex items-center gap-2">
        <Icon name="ph:warning-circle" class="text-xl" /> {{ linksStore.error }}
      </p>
    </div>

    <!-- Loading State -->
    <div v-if="linksStore.loading && linksStore.links.length === 0" class="text-center py-20">
      <Icon name="ph:spinner" class="animate-spin text-4xl text-gray-400 mx-auto mb-4" />
      <p class="font-semibold text-gray-500">Loading your links...</p>
    </div>

    <!-- Empty State -->
    <div v-else-if="linksStore.links.length === 0" class="text-center py-20">
      <div class="w-20 h-20 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
        <Icon name="ph:link-break" class="text-3xl text-gray-400" />
      </div>
      <h3 class="text-xl font-black mb-2">No links yet</h3>
      <p class="text-gray-500 font-semibold mb-6">Add your first link or product to get started.</p>
      <button @click="openCreateModal('standard')"
        class="bg-black text-white font-bold px-8 py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full">
        Add Your First Link
      </button>
    </div>

    <!-- Link Items List (Drag & Drop) -->
    <div v-else class="space-y-4 pt-2" ref="listContainer">
      <VueDraggable
        v-model="dragItems"
        handle=".drag-handle"
        :animation="200"
        ghost-class="opacity-30"
        :on-end="onDragEnd"
        class="space-y-4"
      >
        <div v-for="link in dragItems" :key="link.id"
          class="bg-white p-5 rounded-2xl shadow-[0_2px_8px_rgba(0,0,0,0.04)] border border-gray-200 flex items-start sm:items-center gap-4 transition-all hover:shadow-[0_8px_16px_rgba(0,0,0,0.06)] group">
          <!-- Drag Handle -->
          <div class="drag-handle cursor-grab text-gray-300 hover:text-black mt-2 sm:mt-0 transition-colors">
            <Icon name="ph:dots-six-vertical" class="text-2xl" />
          </div>

          <!-- Product Thumbnail (affiliate only) -->
          <div v-if="link.type === 'affiliate_product'"
            class="w-20 h-20 bg-gray-100 rounded-xl overflow-hidden flex-shrink-0 border border-gray-200 relative group-hover:border-gray-300 transition-colors">
            <img v-if="link.image_url" :src="link.image_url" :alt="link.title" class="w-full h-full object-cover">
            <div v-else class="w-full h-full flex items-center justify-center text-gray-400">
              <Icon name="ph:image" class="text-2xl" />
            </div>
          </div>

          <!-- Content -->
          <div class="flex-1 space-y-2 min-w-0">
            <div class="flex items-center justify-between gap-2">
              <input :value="link.title" @change="updateLinkField(link.id, 'title', ($event.target as HTMLInputElement).value)"
                class="font-bold text-gray-900 bg-transparent border-none focus:ring-0 p-0 text-base w-full outline-none hover:bg-gray-50 focus:bg-gray-50 rounded px-2 -ml-2 transition-colors"
                :placeholder="link.type === 'affiliate_product' ? 'Product name' : 'Link title'">
              <!-- Toggle -->
              <label class="relative inline-flex items-center cursor-pointer ml-2 flex-shrink-0">
                <input type="checkbox" :checked="link.is_active" @change="toggleLink(link)"
                  class="sr-only peer">
                <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-green-500" />
              </label>
            </div>

            <input :value="link.url" @change="updateLinkField(link.id, 'url', ($event.target as HTMLInputElement).value)"
              class="text-sm font-medium text-gray-500 bg-transparent border-none focus:ring-0 p-0 w-full outline-none hover:bg-gray-50 focus:bg-gray-50 rounded px-2 -ml-2 transition-colors"
              placeholder="https://...">

            <div class="flex items-center gap-4 pt-3 text-gray-400 flex-wrap">
              <!-- Type badge -->
              <span v-if="link.type === 'affiliate_product'"
                class="text-xs bg-yellow-100 text-yellow-800 px-2.5 py-1 rounded-md font-bold flex items-center gap-1 border border-yellow-200">
                <Icon name="ph:shopping-bag" /> Affiliate Product
              </span>

              <!-- Add image button (affiliate) -->
              <button v-if="link.type === 'affiliate_product'"
                @click="updateImagePrompt(link)"
                class="hover:text-black transition-colors flex items-center gap-1 text-sm font-semibold">
                <Icon name="ph:image" class="text-lg" />
                <span class="hidden sm:inline">{{ link.image_url ? 'Change Image' : 'Add Image' }}</span>
              </button>

              <!-- Delete -->
              <button @click="handleDelete(link.id)"
                class="hover:text-red-500 transition-colors ml-auto">
                <Icon name="ph:trash" class="text-lg" />
              </button>
            </div>
          </div>
        </div>
      </VueDraggable>
    </div>

    <!-- Create/Edit Modal -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/30" @click.self="closeModal">
      <div class="bg-white border-4 border-black shadow-brutal-lg p-8 w-full max-w-lg relative">
        <button @click="closeModal" class="absolute top-4 right-4 text-gray-400 hover:text-black transition-colors">
          <Icon name="ph:x" class="text-2xl" />
        </button>

        <h2 class="text-2xl font-black mb-6">
          {{ editingLink ? 'Edit' : 'Add' }}
          {{ modalType === 'affiliate_product' ? 'Product' : 'Link' }}
        </h2>

        <form @submit.prevent="handleSave" class="space-y-4">
          <div>
            <label class="block font-bold text-sm mb-2">Title</label>
            <input v-model="form.title" type="text" required
              :placeholder="modalType === 'affiliate_product' ? 'Product name' : 'Link title'"
              class="w-full border-4 border-black py-3 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
          </div>

          <div>
            <label class="block font-bold text-sm mb-2">URL</label>
            <input v-model="form.url" type="url" required placeholder="https://..."
              class="w-full border-4 border-black py-3 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
          </div>

          <div v-if="modalType === 'affiliate_product'">
            <label class="block font-bold text-sm mb-2">Image URL (optional)</label>
            <input v-model="form.image_url" type="url" placeholder="https://..."
              class="w-full border-4 border-black py-3 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
          </div>

          <div class="flex gap-3 pt-4">
            <button type="button" @click="closeModal"
              class="flex-1 bg-white text-black font-bold py-3 border-4 border-black hover:bg-gray-50 transition-all">
              Cancel
            </button>
            <button type="submit" :disabled="linksStore.loading"
              class="flex-1 bg-black text-white font-bold py-3 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all disabled:opacity-50">
              {{ linksStore.loading ? 'Saving...' : 'Save' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'dashboard',
  middleware: 'auth',
})

import { VueDraggable } from 'vue-draggable-plus'
import type { Link, CreateLinkRequest, UpdateLinkRequest } from '~/types'

const linksStore = useLinksStore()
const dragItems = ref<Link[]>([])

// Modal state
const showModal = ref(false)
const editingLink = ref<Link | null>(null)
const modalType = ref<'standard' | 'affiliate_product'>('standard')
const form = ref<CreateLinkRequest>({ title: '', url: '', type: 'standard', image_url: null })

// Watch links for drag items
watch(() => linksStore.sortedLinks, (newLinks) => {
  dragItems.value = [...newLinks]
}, { immediate: true, deep: true })

// Fetch links on mount
onMounted(() => {
  linksStore.fetchLinks()
})

function openCreateModal(type: 'standard' | 'affiliate_product') {
  editingLink.value = null
  modalType.value = type
  form.value = { title: '', url: '', type, image_url: null }
  showModal.value = true
}

function openEditModal(link: Link) {
  editingLink.value = link
  modalType.value = link.type
  form.value = {
    title: link.title,
    url: link.url,
    type: link.type,
    image_url: link.image_url,
  }
  showModal.value = true
}

function closeModal() {
  showModal.value = false
  editingLink.value = null
}

async function handleSave() {
  if (editingLink.value) {
    await linksStore.updateLink(editingLink.value.id, form.value as UpdateLinkRequest)
  } else {
    await linksStore.createLink(form.value as CreateLinkRequest)
  }
  closeModal()
}

async function handleDelete(linkId: string) {
  if (confirm('Are you sure you want to delete this link?')) {
    await linksStore.deleteLink(linkId)
  }
}

async function toggleLink(link: Link) {
  await linksStore.updateLink(link.id, { is_active: !link.is_active })
}

async function updateLinkField(linkId: string, field: string, value: any) {
  await linksStore.updateLink(linkId, { [field]: value })
}

function updateImagePrompt(link: Link) {
  const url = prompt('Enter image URL:', link.image_url || '')
  if (url) {
    linksStore.updateLink(link.id, { image_url: url })
  }
}

// Drag and drop
async function onDragEnd() {
  const items = dragItems.value.map((item, index) => ({
    id: item.id,
    sort_order: index,
  }))
  await linksStore.reorderLinks(items)
}
</script>
