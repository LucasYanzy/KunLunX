<template>
  <div class="sentiment-page">
    <!-- Fear & Greed Gauge -->
    <div class="top-row">
      <div class="glass-card gauge-card">
        <h2>恐惧与贪婪指数</h2>
        <div ref="gaugeRef" class="gauge-chart" style="height: 280px"></div>
        <div class="gauge-label mono-num">
          <span class="gauge-value">{{ fearGreed.value }}</span>
          <span :class="labelClass">{{ fearGreed.label }}</span>
        </div>
      </div>

      <!-- Momentum -->
      <div class="glass-card momentum-card">
        <h2>市场动量</h2>
        <div class="momentum-grid">
          <div v-for="m in momentumData" :key="m.index" class="momentum-item">
            <span class="momentum-name">{{ m.index }}</span>
            <span class="mono-num" :class="m.rsi > 70 ? 'price-up' : m.rsi < 30 ? 'price-down' : ''">
              RSI: {{ m.rsi.toFixed(1) }}
            </span>
            <el-tag :type="m.rsi > 70 ? 'danger' : m.rsi < 30 ? 'success' : 'info'" size="small">
              {{ m.rsi > 70 ? '超买' : m.rsi < 30 ? '超卖' : '中性' }}
            </el-tag>
          </div>
        </div>
      </div>
    </div>

    <!-- Historical Chart -->
    <div class="glass-card history-section">
      <div class="section-header">
        <h2>恐惧贪婪历史走势</h2>
        <el-radio-group v-model="historyRange" size="small">
          <el-radio-button label="1m">1个月</el-radio-button>
          <el-radio-button label="3m">3个月</el-radio-button>
          <el-radio-button label="1y">1年</el-radio-button>
        </el-radio-group>
      </div>
      <div ref="historyRef" class="chart-container" style="height: 300px"></div>
    </div>

    <!-- VIX & Breadth -->
    <div class="bottom-row">
      <div class="glass-card">
        <h3>VIX 波动率指数</h3>
        <div class="mono-num vix-value">{{ vix.value }}</div>
        <div class="text-kunlun-muted text-xs">{{ vix.status }}</div>
      </div>
      <div class="glass-card">
        <h3>市场广度 (涨跌家数)</h3>
        <div class="mono-num">涨 <span class="price-up">{{ breadth.up }}</span> / 跌 <span class="price-down">{{ breadth.down }}</span></div>
      </div>
      <div class="glass-card">
        <h3>融资融券余额</h3>
        <div class="mono-num">{{ margin.balance }}亿</div>
        <div :class="margin.change >= 0 ? 'price-up' : 'price-down'" class="mono-num text-sm">
          {{ margin.change >= 0 ? '+' : '' }}{{ margin.change }}亿
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

const historyRange = ref('1m')
const gaugeRef = ref<HTMLElement>()
const historyRef = ref<HTMLElement>()

// Placeholder data
const fearGreed = ref({ value: 42, label: '恐惧' })
const momentumData = ref([
  { index: '标普500', rsi: 55.3 },
  { index: '沪深300', rsi: 38.7 },
  { index: '纳斯达克', rsi: 72.1 },
])
const vix = ref({ value: 18.42, status: '低波动' })
const breadth = ref({ up: 1823, down: 2417 })
const margin = ref({ balance: 15832, change: -127 })

const labelClass = computed(() => {
  const v = fearGreed.value.value
  if (v <= 20) return 'label-extreme-fear'
  if (v <= 40) return 'label-fear'
  if (v <= 60) return 'label-neutral'
  if (v <= 80) return 'label-greed'
  return 'label-extreme-greed'
})

onMounted(() => {
  // TODO: init ECharts gauge and history line chart
})
</script>

<style scoped>
.sentiment-page {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.top-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.gauge-card, .momentum-card {
  padding: 20px;
}

.gauge-label {
  text-align: center;
  margin-top: 8px;
}

.gauge-value {
  font-size: 48px;
  font-weight: 700;
  margin-right: 12px;
}

.label-extreme-fear { color: #22C55E; }
.label-fear { color: #86EFAC; }
.label-neutral { color: var(--kl-muted); }
.label-greed { color: #FCA5A5; }
.label-extreme-greed { color: #EF4444; }

.momentum-grid {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 16px;
}

.momentum-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  border-radius: 6px;
  background: rgba(48, 54, 61, 0.3);
}

.momentum-name {
  font-size: 14px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.history-section {
  padding: 20px;
}

.bottom-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 12px;
}

.bottom-row .glass-card {
  padding: 20px;
  text-align: center;
}

.vix-value {
  font-size: 32px;
  font-weight: 700;
  margin: 8px 0;
}
</style>
