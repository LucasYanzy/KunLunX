import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    redirect: '/dashboard',
  },
  {
    path: '/dashboard',
    name: 'GlobalDashboard',
    component: () => import('@/modules/global-dashboard/index.vue'),
    meta: { title: '全球看板', icon: 'Monitor' },
  },
  {
    path: '/cloudmap',
    name: 'CloudMap',
    component: () => import('@/modules/global-dashboard/CloudMap.vue'),
    meta: { title: '大盘云图', icon: 'Grid' },
  },
  {
    path: '/analyzer',
    name: 'StockAnalyzer',
    component: () => import('@/modules/stock-analyzer/index.vue'),
    meta: { title: '个股诊断', icon: 'DataAnalysis' },
  },
  {
    path: '/sentiment',
    name: 'Sentiment',
    component: () => import('@/modules/sentiment/index.vue'),
    meta: { title: '市场情绪', icon: 'TrendCharts' },
  },
  {
    path: '/news',
    name: 'NewsFactory',
    component: () => import('@/modules/news-factory/index.vue'),
    meta: { title: '新闻因子', icon: 'Tickets' },
  },
  {
    path: '/lab',
    name: 'StrategyLab',
    component: () => import('@/modules/strategy-lab/index.vue'),
    meta: { title: '策略实验室', icon: 'MagicStick' },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
