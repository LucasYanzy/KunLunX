import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useSettingsStore = defineStore('settings', () => {
  const refreshInterval = ref(5000)    // ms
  const defaultMarket = ref('cn')
  const theme = ref<'dark' | 'light'>('dark')

  function setRefreshInterval(ms: number) {
    refreshInterval.value = ms
  }

  function setDefaultMarket(market: string) {
    defaultMarket.value = market
  }

  return { refreshInterval, defaultMarket, theme, setRefreshInterval, setDefaultMarket }
})
