<template>
  <div class="lab-page">
    <div class="lab-layout">
      <!-- Code Editor -->
      <div class="glass-card editor-panel">
        <div class="panel-header">
          <h2>策略编辑器</h2>
          <div class="panel-actions">
            <el-select v-model="selectedTemplate" placeholder="加载模板" size="small" style="width: 160px">
              <el-option label="均线交叉" value="sma_cross" />
              <el-option label="RSI超买超卖" value="rsi" />
              <el-option label="动量策略" value="momentum" />
              <el-option label="配对交易" value="pairs" />
            </el-select>
            <el-button type="primary" @click="runBacktest" :loading="running">
              ▶ 运行回测
            </el-button>
          </div>
        </div>
        <!-- Monaco Editor will mount here -->
        <div ref="editorRef" class="code-editor"></div>
      </div>

      <!-- Parameters -->
      <div class="glass-card params-panel">
        <h3>回测参数</h3>
        <el-form label-position="top" size="small">
          <el-form-item label="股票代码">
            <el-input v-model="params.ticker" placeholder="AAPL" />
          </el-form-item>
          <el-form-item label="时间范围">
            <el-date-picker
              v-model="params.dateRange"
              type="daterange"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
            />
          </el-form-item>
          <el-form-item label="初始资金">
            <el-input-number v-model="params.capital" :min="1000" :step="10000" />
          </el-form-item>
          <el-form-item label="手续费率">
            <el-input-number v-model="params.commission" :min="0" :max="0.01" :step="0.0001" :precision="4" />
          </el-form-item>
          <el-form-item label="滑点">
            <el-input-number v-model="params.slippage" :min="0" :max="0.01" :step="0.0001" :precision="4" />
          </el-form-item>
        </el-form>
      </div>
    </div>

    <!-- Results -->
    <div v-if="result" class="results-section">
      <!-- Metrics Cards -->
      <div class="metrics-row">
        <div class="glass-card metric">
          <span class="metric-label">年化收益</span>
          <span class="mono-num metric-value" :class="result.annual_return >= 0 ? 'price-up' : 'price-down'">
            {{ (result.annual_return * 100).toFixed(2) }}%
          </span>
        </div>
        <div class="glass-card metric">
          <span class="metric-label">夏普比率</span>
          <span class="mono-num metric-value">{{ result.sharpe_ratio.toFixed(2) }}</span>
        </div>
        <div class="glass-card metric">
          <span class="metric-label">最大回撤</span>
          <span class="mono-num metric-value price-down">{{ (result.max_drawdown * 100).toFixed(2) }}%</span>
        </div>
        <div class="glass-card metric">
          <span class="metric-label">胜率</span>
          <span class="mono-num metric-value">{{ (result.win_rate * 100).toFixed(1) }}%</span>
        </div>
        <div class="glass-card metric">
          <span class="metric-label">交易次数</span>
          <span class="mono-num metric-value">{{ result.total_trades }}</span>
        </div>
      </div>

      <!-- Equity Curve -->
      <div class="glass-card equity-section">
        <h3>净值曲线</h3>
        <div ref="equityRef" class="chart-container" style="height: 300px"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const selectedTemplate = ref('')
const running = ref(false)
const editorRef = ref<HTMLElement>()
const equityRef = ref<HTMLElement>()

const params = ref({
  ticker: 'AAPL',
  dateRange: null as any,
  capital: 100000,
  commission: 0.001,
  slippage: 0.001,
})

const result = ref<any>(null)

async function runBacktest() {
  running.value = true
  // TODO: POST to /api/v1/strategy/backtest
  running.value = false
}
</script>

<style scoped>
.lab-page {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.lab-layout {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 16px;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.panel-actions {
  display: flex;
  gap: 8px;
}

.editor-panel {
  padding: 20px;
}

.code-editor {
  height: 400px;
  background: #0D1117;
  border: 1px solid var(--kl-border);
  border-radius: 8px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  padding: 12px;
  color: var(--kl-text);
  overflow: auto;
}

.params-panel {
  padding: 20px;
}

.results-section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.metrics-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
}

.metric {
  text-align: center;
  padding: 16px;
}

.metric-label {
  font-size: 12px;
  color: var(--kl-muted);
  display: block;
  margin-bottom: 4px;
}

.metric-value {
  font-size: 24px;
  font-weight: 700;
}

.equity-section {
  padding: 20px;
}
</style>
