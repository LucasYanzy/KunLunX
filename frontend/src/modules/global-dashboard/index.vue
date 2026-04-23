<template>
  <div class="dashboard-page">
    <!-- World Map Section -->
    <section class="glass-card map-section">
      <div class="section-header">
        <h2>全球市场热力图</h2>
        <el-radio-group v-model="region" size="small">
          <el-radio-button label="all">全部</el-radio-button>
          <el-radio-button label="americas">美洲</el-radio-button>
          <el-radio-button label="europe">欧洲</el-radio-button>
          <el-radio-button label="asia">亚洲</el-radio-button>
        </el-radio-group>
      </div>
      <div ref="mapRef" class="chart-container" style="height: 400px"></div>
    </section>

    <!-- Index Cards -->
    <section class="index-cards">
      <div v-for="idx in majorIndices" :key="idx.ticker" class="glass-card index-card">
        <div class="index-name">{{ idx.name }}</div>
        <div class="mono-num index-price">{{ idx.price.toFixed(2) }}</div>
        <div :class="idx.change >= 0 ? 'price-up' : 'price-down'" class="mono-num">
          {{ idx.change >= 0 ? '+' : '' }}{{ idx.change_pct.toFixed(2) }}%
        </div>
      </div>
    </section>

    <!-- Category Tabs -->
    <section class="glass-card tabs-section">
      <el-tabs v-model="activeTab">
        <el-tab-pane label="指数期货" name="futures" />
        <el-tab-pane label="商品期货" name="commodities" />
        <el-tab-pane label="外汇" name="forex" />
        <el-tab-pane label="债券" name="bonds" />
        <el-tab-pane label="数字货币" name="crypto" />
      </el-tabs>
      <!-- Tab content placeholder -->
      <div class="tab-content">
        <p class="text-kunlun-muted">{{ activeTab }} data will load here</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const region = ref('all')
const activeTab = ref('futures')
const mapRef = ref<HTMLElement>()

// Placeholder data — will be replaced by API calls
const majorIndices = ref([
  { ticker: 'DJI', name: '道琼斯', price: 39872.99, change: 66.22, change_pct: 0.17 },
  { ticker: 'IXIC', name: '纳斯达克', price: 16832.62, change: -7.52, change_pct: -0.04 },
  { ticker: 'SPX', name: '标普500', price: 5321.41, change: 13.28, change_pct: 0.25 },
  { ticker: 'SSEC', name: '上证指数', price: 3154.03, change: -17.92, change_pct: -0.56 },
  { ticker: 'SZCOMP', name: '深证成指', price: 9788.37, change: -62.15, change_pct: -0.63 },
  { ticker: 'HSI', name: '恒生指数', price: 19553.61, change: 177.08, change_pct: 0.91 },
])

onMounted(() => {
  // TODO: init ECharts world map here
})
</script>

<style scoped>
.dashboard-page {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.index-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 12px;
}

.index-card {
  text-align: center;
}

.index-name {
  font-size: 13px;
  color: var(--kl-muted);
  margin-bottom: 4px;
}

.index-price {
  font-size: 20px;
  font-weight: 600;
}

.tabs-section {
  padding: 16px;
}

.tab-content {
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
