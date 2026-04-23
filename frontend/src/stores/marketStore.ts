import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

export const useMarketStore = defineStore('market', () => {
  const indices = ref<any[]>([])
  const cloudMapData = ref<any>(null)
  const loading = ref(false)

  async function fetchIndices() {
    loading.value = true
    try {
      const { data } = await api.get('/market/indices')
      indices.value = data.data
    } catch (e) {
      console.error('Failed to fetch indices:', e)
    } finally {
      loading.value = false
    }
  }

  async function fetchCloudMap(market: string = 'cn') {
    try {
      const { data } = await api.get(`/market/cloudmap/${market}`)
      cloudMapData.value = data.data
    } catch (e) {
      console.error('Failed to fetch cloud map:', e)
    }
  }

  return { indices, cloudMapData, loading, fetchIndices, fetchCloudMap }
})
