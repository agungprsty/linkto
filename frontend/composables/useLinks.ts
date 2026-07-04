import { useLinksStore } from '~/stores/links'
import type { CreateLinkRequest, UpdateLinkRequest } from '~/types'

export function useLinks() {
  const linksStore = useLinksStore()

  // Computed
  const links = computed(() => linksStore.sortedLinks)
  const activeLinks = computed(() => linksStore.activeLinks)
  const loading = computed(() => linksStore.loading)
  const error = computed(() => linksStore.error)

  // Methods
  async function fetchLinks() {
    await linksStore.fetchLinks()
  }

  async function createLink(req: CreateLinkRequest) {
    return await linksStore.createLink(req)
  }

  async function updateLink(linkId: string, req: UpdateLinkRequest) {
    return await linksStore.updateLink(linkId, req)
  }

  async function deleteLink(linkId: string) {
    return await linksStore.deleteLink(linkId)
  }

  async function reorderLinks(items: { id: string; sort_order: number }[]) {
    return await linksStore.reorderLinks(items)
  }

  function updateLocalOrder(items: any[]) {
    linksStore.updateLocalOrder(items)
  }

  return {
    links,
    activeLinks,
    loading,
    error,
    fetchLinks,
    createLink,
    updateLink,
    deleteLink,
    reorderLinks,
    updateLocalOrder,
  }
}
