<template>
  <div class="news-page">
    <!-- Live News Ticker -->
    <div class="glass-card ticker-bar">
      <div class="ticker-scroll">
        <span v-for="(n, i) in latestNews" :key="i" class="ticker-item">
          <el-tag :type="n.sentiment === 'positive' ? 'danger' : n.sentiment === 'negative' ? 'success' : 'info'" size="small">
            {{ n.sentiment === 'positive' ? '利好' : n.sentiment === 'negative' ? '利空' : '中性' }}
          </el-tag>
          {{ n.title }}
          <span class="ticker-source">— {{ n.source }}</span>
        </span>
      </div>
    </div>

    <div class="news-layout">
      <!-- News List -->
      <div class="glass-card news-list">
        <h2>实时新闻流</h2>
        <div v-for="article in latestNews" :key="article.url" class="news-item">
          <div class="news-header">
            <el-tag size="small" :type="sentimentTag(article.sentiment)">
              {{ article.sentiment }}
            </el-tag>
            <span class="news-source">{{ article.source }}</span>
            <span class="news-time mono-num">{{ article.time }}</span>
          </div>
          <h3 class="news-title">{{ article.title }}</h3>
          <p class="news-summary">{{ article.summary }}</p>
          <div class="news-tags">
            <el-tag v-for="kw in article.keywords" :key="kw" size="small" type="info">
              {{ kw }}
            </el-tag>
          </div>
        </div>
      </div>

      <!-- Factor Panel -->
      <div class="glass-card factor-panel">
        <h2>AI 因子生成</h2>
        <div class="hot-keywords">
          <h3>高频热词 (24h)</h3>
          <div v-for="kw in hotKeywords" :key="kw.word" class="keyword-item">
            <span class="keyword-word">{{ kw.word }}</span>
            <el-progress
              :percentage="kw.frequency"
              :color="kw.sentiment > 0 ? '#EF4444' : '#22C55E'"
              :stroke-width="8"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// Placeholder data
const latestNews = ref([
  {
    title: '美联储维持利率不变，市场反应平淡',
    source: 'Reuters',
    url: '#',
    time: '14:32',
    summary: '美联储在最新的议息会议上决定维持当前利率水平不变...',
    sentiment: 'neutral',
    keywords: ['美联储', '利率', '货币政策'],
  },
  {
    title: '英伟达Q4财报超预期，盘后大涨8%',
    source: '新浪财经',
    url: '#',
    time: '09:15',
    summary: '英伟达公布第四季度财报，营收和利润均超出华尔街预期...',
    sentiment: 'positive',
    keywords: ['英伟达', 'AI芯片', '财报'],
  },
])

const hotKeywords = ref([
  { word: 'AI芯片', frequency: 85, sentiment: 0.7 },
  { word: '降息', frequency: 72, sentiment: -0.2 },
  { word: '新能源', frequency: 60, sentiment: 0.3 },
  { word: '地缘风险', frequency: 45, sentiment: -0.8 },
])

function sentimentTag(s: string) {
  if (s === 'positive') return 'danger'
  if (s === 'negative') return 'success'
  return 'info'
}
</script>

<style scoped>
.news-page {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ticker-bar {
  padding: 8px 16px;
  overflow: hidden;
  white-space: nowrap;
}

.ticker-scroll {
  display: flex;
  gap: 40px;
  animation: scroll 30s linear infinite;
}

@keyframes scroll {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

.ticker-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  flex-shrink: 0;
}

.ticker-source {
  color: var(--kl-muted);
  font-size: 11px;
}

.news-layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 16px;
}

.news-list {
  padding: 20px;
  max-height: calc(100vh - 240px);
  overflow-y: auto;
}

.news-item {
  padding: 16px 0;
  border-bottom: 1px solid var(--kl-border);
}

.news-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}

.news-source, .news-time {
  font-size: 11px;
  color: var(--kl-muted);
}

.news-title {
  font-size: 15px;
  font-weight: 500;
  margin-bottom: 4px;
}

.news-summary {
  font-size: 13px;
  color: var(--kl-muted);
  margin-bottom: 8px;
}

.news-tags {
  display: flex;
  gap: 4px;
}

.factor-panel {
  padding: 20px;
}

.hot-keywords {
  margin-top: 16px;
}

.keyword-item {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.keyword-word {
  min-width: 80px;
  font-size: 14px;
}
</style>
