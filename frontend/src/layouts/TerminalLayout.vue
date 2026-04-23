<template>
  <div class="terminal-layout">
    <!-- ─── Sidebar ─────────────────────────────────── -->
    <aside class="sidebar glass-panel">
      <div class="logo">
        <span class="logo-icon">🏔️</span>
        <span v-if="!collapsed" class="logo-text">KunLun</span>
      </div>

      <nav class="nav-menu">
        <router-link
          v-for="item in menuItems"
          :key="item.path"
          :to="item.path"
          class="nav-item"
          active-class="nav-item--active"
        >
          <el-icon><component :is="item.icon" /></el-icon>
          <span v-if="!collapsed" class="nav-label">{{ item.label }}</span>
        </router-link>
      </nav>

      <button class="collapse-btn" @click="collapsed = !collapsed">
        <el-icon><Fold v-if="!collapsed" /><Expand v-else /></el-icon>
      </button>
    </aside>

    <!-- ─── Main Content ────────────────────────────── -->
    <main class="main-content">
      <!-- Top Bar -->
      <header class="topbar glass-panel">
        <div class="topbar-left">
          <h1 class="page-title">{{ currentTitle }}</h1>
        </div>
        <div class="topbar-right">
          <span class="mono-num text-xs text-kunlun-muted">
            {{ currentTime }}
          </span>
        </div>
      </header>

      <!-- Router View -->
      <div class="content-area">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import {
  Monitor, Grid, DataAnalysis, TrendCharts,
  Tickets, MagicStick, Fold, Expand
} from '@element-plus/icons-vue'

const route = useRoute()
const collapsed = ref(false)
const currentTime = ref('')

const menuItems = [
  { path: '/dashboard', label: '全球看板', icon: Monitor },
  { path: '/cloudmap',  label: '大盘云图', icon: Grid },
  { path: '/analyzer',  label: '个股诊断', icon: DataAnalysis },
  { path: '/sentiment', label: '市场情绪', icon: TrendCharts },
  { path: '/news',      label: '新闻因子', icon: Tickets },
  { path: '/lab',       label: '策略实验室', icon: MagicStick },
]

const currentTitle = computed(() => {
  const meta = route.meta as { title?: string }
  return meta.title || 'KunLun Terminal Pro'
})

let timer: number
onMounted(() => {
  const tick = () => {
    currentTime.value = new Date().toLocaleString('zh-CN', {
      hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit'
    })
  }
  tick()
  timer = window.setInterval(tick, 1000)
})
onUnmounted(() => clearInterval(timer))
</script>

<style scoped>
.terminal-layout {
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

/* ─── Sidebar ───────────────────── */
.sidebar {
  display: flex;
  flex-direction: column;
  width: 220px;
  padding: 16px 12px;
  gap: 8px;
  transition: width 0.3s ease;
  flex-shrink: 0;
  border-radius: 0;
  border-right: 1px solid var(--kl-border);
  border-top: none;
  border-bottom: none;
  border-left: none;
}

.sidebar:has(.collapse-btn:only-child) {
  width: 64px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  margin-bottom: 16px;
}
.logo-icon { font-size: 24px; }
.logo-text {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  font-size: 18px;
  background: linear-gradient(135deg, var(--kl-cyan), var(--kl-magenta));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-menu {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 8px;
  color: var(--kl-muted);
  text-decoration: none;
  font-size: 14px;
  transition: all 0.2s ease;
}
.nav-item:hover {
  color: var(--kl-text);
  background: rgba(48, 54, 61, 0.5);
}
.nav-item--active {
  color: var(--kl-cyan) !important;
  background: rgba(0, 245, 255, 0.08) !important;
  border-left: 2px solid var(--kl-cyan);
}

.collapse-btn {
  background: none;
  border: none;
  color: var(--kl-muted);
  cursor: pointer;
  padding: 8px;
}

/* ─── Main ──────────────────────── */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 24px;
  border-radius: 0;
  border-bottom: 1px solid var(--kl-border);
  flex-shrink: 0;
}

.page-title {
  font-size: 16px;
  font-weight: 600;
}

.content-area {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

/* ─── Transitions ───────────────── */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
