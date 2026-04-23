<template>
  <div class="analyzer-page">
    <!-- Search Bar -->
    <div class="glass-card search-section">
      <el-input
        v-model="ticker"
        placeholder="输入股票代码 (AAPL / 600519.SH / 0700.HK)"
        size="large"
        @keyup.enter="runDiagnosis"
      >
        <template #append>
          <el-button @click="runDiagnosis" :loading="loading">诊断</el-button>
        </template>
      </el-input>
    </div>

    <!-- Score Overview -->
    <div v-if="result" class="score-grid">
      <div class="glass-card score-card">
        <div class="score-label">基本面评分</div>
        <div class="mono-num score-value">{{ result.fundamental_score }}</div>
        <div class="score-weight">权重 60%</div>
      </div>
      <div class="glass-card score-card">
        <div class="score-label">技术 & 情感评分</div>
        <div class="mono-num score-value">{{ result.technical_score }}</div>
        <div class="score-weight">权重 40%</div>
      </div>
      <div class="glass-card score-card score-card--total">
        <div class="score-label">综合评分</div>
        <div class="mono-num score-value score-total">{{ result.total_score }}</div>
        <div class="rating-badge" :class="'rating-' + result.rating">
          {{ result.rating }}
        </div>
      </div>
    </div>

    <!-- 72-dim Data Table -->
    <div v-if="result" class="glass-card metrics-section">
      <h3>72 维基础数据解剖</h3>
      <el-descriptions :column="3" border size="small">
        <el-descriptions-item label="市值">{{ result.market_cap }}</el-descriptions-item>
        <el-descriptions-item label="PE">{{ result.pe_ratio }}</el-descriptions-item>
        <el-descriptions-item label="PB">{{ result.pb_ratio }}</el-descriptions-item>
        <el-descriptions-item label="ROE">{{ result.roe }}%</el-descriptions-item>
        <el-descriptions-item label="FCF">{{ result.fcf }}</el-descriptions-item>
        <el-descriptions-item label="Beta">{{ result.beta }}</el-descriptions-item>
        <el-descriptions-item label="股息率">{{ result.dividend_yield }}%</el-descriptions-item>
      </el-descriptions>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const ticker = ref('')
const loading = ref(false)
const result = ref<any>(null)

async function runDiagnosis() {
  if (!ticker.value) return
  loading.value = true
  // TODO: call /api/v1/stock/diagnose/{ticker}
  loading.value = false
}
</script>

<style scoped>
.analyzer-page {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.search-section {
  padding: 20px;
}

.score-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 12px;
}

.score-card {
  text-align: center;
  padding: 24px;
}

.score-label {
  font-size: 13px;
  color: var(--kl-muted);
}

.score-value {
  font-size: 36px;
  font-weight: 700;
  margin: 8px 0;
}

.score-total {
  color: var(--kl-cyan);
}

.score-weight {
  font-size: 11px;
  color: var(--kl-muted);
}

.rating-badge {
  display: inline-block;
  padding: 4px 16px;
  border-radius: 4px;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
}

.rating-S { background: var(--kl-cyan); color: var(--kl-bg); }
.rating-A { background: #22C55E; color: var(--kl-bg); }
.rating-B { background: #EAB308; color: var(--kl-bg); }
.rating-C { background: #F97316; color: var(--kl-bg); }
.rating-D { background: #EF4444; color: var(--kl-bg); }

.metrics-section {
  padding: 20px;
}

.metrics-section h3 {
  margin-bottom: 12px;
}
</style>
