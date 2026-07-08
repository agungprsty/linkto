import { defineStore } from 'pinia'
import type { Link, CreateLinkRequest, UpdateLinkRequest, ReorderLinksRequest } from '~/types'

export const useLinksStore = defineStore('links', () => {
  // State
  const links = ref<Link[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  // Getters
  const sortedLinks = computed(() => {
    return [...links.value].sort((a, b) => a.sort_order - b.sort_order)
  })

  const activeLinks = computed(() => {
    return sortedLinks.value.filter(l => l.is_active)
  })

  // Actions
  async function fetchLinks(): Promise<void> {
    loading.value = true
    error.value = null
    try {
      const { $api } = useNuxtApp()
      const data = await $api('/links') as Link[]
      links.value = data
    } catch (e: any) {
      error.value = e?.data?.detail?.message || e?.message || 'Failed to fetch links'
    } finally {
      loading.value = false
    }
  }

  async function createLink(req: CreateLinkRequest): Promise<Link | null> {
    loading.value = true
    error.value = null
    try {
      const { $api } = useNuxtApp()
      const data = await $api('/links', {
        method: 'POST',
        body: req,
      }) as Link
      links.value.push(data)
      return data
    } catch (e: any) {
      error.value = e?.data?.detail?.message || e?.message || 'Failed to create link'
      return null
    } finally {
      loading.value = false
    }
  }

  async function updateLink(linkId: string, req: UpdateLinkRequest): Promise<Link | null> {
    error.value = null
    try {
      const { $api } = useNuxtApp()
      const data = await $api(`/links/${linkId}`, {
        method: 'PUT',
        body: req,
      }) as Link
      const idx = links.value.findIndex(l => l.id === linkId)
      if (idx !== -1) {
        links.value[idx] = data
      }
      return data
    } catch (e: any) {
      error.value = e?.data?.detail?.message || e?.message || 'Failed to update link'
      return null
    }
  }

  async function deleteLink(linkId: string): Promise<boolean> {
    error.value = null
    try {
      const { $api } = useNuxtApp()
      await $api(`/links/${linkId}`, { method: 'DELETE' })
      links.value = links.value.filter(l => l.id !== linkId)
      return true
    } catch (e: any) {
      error.value = e?.data?.detail?.message || e?.message || 'Failed to delete link'
      return false
    }
  }

  async function reorderLinks(items: { id: string; sort_order: number }[]): Promise<boolean> {
    error.value = null
    try {
      const { $api } = useNuxtApp()
      const data = await $api('/links/reorder', {
        method: 'PUT',
        body: { items },
      }) as Link[]

      // Update local state with reordered data
      links.value = data
      return true
    } catch (e: any) {
      error.value = e?.data?.detail?.message || e?.message || 'Failed to reorder links'
      return false
    }
  }

  // Optimistic update for drag-drop
  function updateLocalOrder(items: Link[]) {
    links.value = items
  }

  function $reset() {
    links.value = []
    loading.value = false
    error.value = null
  }

  return {
    links,
    loading,
    error,
    sortedLinks,
    activeLinks,
    fetchLinks,
    createLink,
    updateLink,
    deleteLink,
    reorderLinks,
    updateLocalOrder,
    $reset,
  }
})
