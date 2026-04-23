<template>
  <div class="cloudmap-page">
    <div class="cloudmap-controls glass-card">
      <el-radio-group v-model="market" size="small">
        <el-radio-button label="cn">沪深 A 股</el-radio-button>
        <el-radio-button label="us">美股</el-radio-button>
        <el-radio-button label="hk">港股</el-radio-button>
      </el-radio-group>
      <el-radio-group v-model="groupBy" size="small">
        <el-radio-button label="sector">按行业</el-radio-button>
        <el-radio-button label="concept">按概念</el-radio-button>
        <el-radio-button label="cap">按市值</el-radio-button>
      </el-radio-group>
    </div>
    <div ref="treemapRef" class="treemap-container glass-card"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'

const market = ref('cn')
const groupBy = ref('sector')
const treemapRef = ref<HTMLElement>()

onMounted(() => {
  // TODO: init ECharts treemap with dapanyuntu-style visual mapping
  // Red = up, Green = down, size = market cap, depth = change_pct magnitude
})

watch([market, groupBy], () => {
  // TODO: re-fetch data and redraw treemap
})
</script>

<style scoped>
.cloudmap-page {
  display: flex;
  flex-direction: column;
  gap: 12px;
  height: calc(100vh - 120px);
}

.cloudmap-controls {
  display: flex;
  gap: 16px;
  padding: 12px 16px;
}

.treemap-container {
  flex: 1;
  min-height: 500px;
}
</style>
