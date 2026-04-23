# 🏔️ KunLun Terminal Pro (昆仑量化终端)

**全球化 · 模块化 · 智能化 — 一站式量化投研终端**

[![Vue3](https://img.shields.io/badge/Frontend-Vue%203%20+%20TypeScript-42b883?logo=vue.js)](https://vuejs.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![VectorBT](https://img.shields.io/badge/Engine-VectorBT%20Pro-orange)](https://vectorbt.dev/)
[![Redis](https://img.shields.io/badge/Cache-Redis%207-DC382D?logo=redis)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Deploy-Docker-2496ED?logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📌 项目愿景

KunLun Terminal Pro 旨在为量化交易者提供一个**媲美 Bloomberg Terminal 的开源替代方案**。
通过严格的模块化设计，开发者可以像搭积木一样逐步构建功能，避免"脑雾"——每个模块独立开发、独立测试、独立部署。

---

## 🧩 六大核心模块

| 模块 | 路由 | 功能概述 | 阶段 |
| :--- | :--- | :--- | :---: |
| 🌐 **全球看板** | `/dashboard` | 世界地图热力图、主要指数实时行情卡片、分类标签页（期货/外汇/债券/加密货币） | Phase 1 |
| 🗺️ **大盘云图** | `/cloudmap` | 复刻 dapanyuntu.com 视觉体验，按行业/概念/市值分组，缩放拖拽，红涨绿跌 | Phase 1 |
| 🔬 **个股诊断** | `/analyzer` | 72 维全息扫描，基本面 (60%) + 技术情感 (40%) 评分，S/A/B/C/D 智能评级 | Phase 2 |
| 📊 **市场情绪** | `/sentiment` | 贪恐指数、VIX 波动率、动量 RSI/MACD、市场广度、融资融券余额 | Phase 2 |
| 📰 **新闻因子** | `/news` | 实时新闻滚动，Claude AI 情感分析，高频热词提取，自动生成量化因子 | Phase 3 |
| 🧪 **策略实验室** | `/lab` | Python 策略编辑器，VectorBT Pro 高速回测，净值曲线 / 夏普 / 最大回撤 | Phase 3 |

### 🔮 预留扩展模块（Planned）

> 以下模块已预留接口和目录结构，后续可直接接入核心框架，无需修改已有代码。

| 模块 | 路由 | 功能概述 | 状态 |
| :--- | :--- | :--- | :---: |
| 💰 **组合管理** | `/portfolio` | 多账户持仓管理、风险敞口分析、资产配置优化 | 💡 预留 |
| 📡 **实时盯盘** | `/watchlist` | 自定义自选股列表、价格预警、分时走势、Level-2 盘口 | 💡 预留 |
| 🤖 **AI 研报** | `/ai-report` | 基于 Claude 自动生成个股/行业研究报告 | 💡 预留 |
| 🔗 **链上数据** | `/onchain` | 巨鲸钱包追踪、DeFi TVL 监控、NFT 热度 | 💡 预留 |
| 🏦 **宏观经济** | `/macro` | 全球央行利率日历、CPI/PMI 数据追踪、收益率曲线 | 💡 预留 |
| ⚙️ **因子仓库** | `/factors` | 多因子模型管理、因子 IC/IR 分析、因子合成与回测 | 💡 预留 |
| 📱 **移动终端** | `/mobile` | 精简版交易仪表盘、推送通知、远程监控 | 💡 预留 |

新增模块只需在 `frontend/src/modules/` 创建目录 + 在 `backend/app/api/v1/` 添加路由即可自动接入系统。

---

## 🏗️ 技术栈

| 层级 | 技术选型 | 说明 |
| :--- | :--- | :--- |
| **前端** | Vue 3 + TypeScript + Vite | Element Plus 组件库，TailwindCSS 原子化样式 |
| **可视化** | ECharts 5 | 世界地图、TreeMap 云图、K 线、仪表盘 |
| **视觉** | Glassmorphism + JetBrains Mono | 毛玻璃暗黑主题，**严格红涨绿跌**，极客等宽字体 |
| **后端** | FastAPI + Python 3.11+ | 异步非阻塞，自动生成 OpenAPI 文档 |
| **数据** | yFinance / AkShare / Binance | 多源适配器 + 自动故障切换 |
| **缓存** | Redis 7 | Tick 5s / K线 60s / 日线 3600s 分级 TTL |
| **存储** | SQLite + Parquet | 配置持久化 + 历史大数据列存储 |
| **AI** | Anthropic Claude API | 新闻语义分析、因子生成 |
| **回测** | VectorBT Pro | 百万级数据点秒级向量化回测 |
| **部署** | Docker Compose | 一键启动 Backend + Frontend + Redis |

---

## 📂 项目结构

```text
KunLun_Terminal Pro/
│
├── frontend/                          # Vue 3 前端应用
│   ├── src/
│   │   ├── modules/                   # ★ 业务模块（核心）
│   │   │   ├── global-dashboard/      #   全球看板 + 大盘云图
│   │   │   ├── stock-analyzer/        #   个股 72 维诊断
│   │   │   ├── sentiment/             #   贪恐指数 + 动量
│   │   │   ├── news-factory/          #   AI 新闻因子
│   │   │   └── strategy-lab/          #   策略回测实验室
│   │   ├── layouts/                   #   终端布局（毛玻璃侧栏 + 顶栏）
│   │   ├── router/                    #   路由（懒加载各模块）
│   │   ├── stores/                    #   Pinia 状态管理
│   │   ├── styles/                    #   全局 CSS 设计令牌
│   │   └── utils/                     #   Axios API 客户端
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── backend/                           # FastAPI 后端
│   ├── main.py                        #   应用入口（注册所有路由）
│   ├── app/
│   │   ├── api/v1/                    #   REST API 路由
│   │   │   ├── market.py              #     全球看板 + 云图
│   │   │   ├── stock.py               #     个股诊断
│   │   │   ├── sentiment.py           #     市场情绪
│   │   │   ├── news.py                #     新闻因子
│   │   │   └── strategy.py            #     策略回测
│   │   ├── services/                  #   业务逻辑层
│   │   │   ├── market_service.py
│   │   │   ├── stock_service.py
│   │   │   ├── sentiment_service.py
│   │   │   ├── news_service.py
│   │   │   └── strategy_service.py
│   │   ├── engines/                   #   计算引擎
│   │   │   ├── backtest.py            #     VectorBT 回测引擎
│   │   │   ├── sentiment.py           #     贪恐指数计算
│   │   │   └── factor.py              #     NLP 因子提取
│   │   ├── data/                      #   数据层
│   │   │   ├── adapters/              #     多源适配器（可插拔）
│   │   │   │   ├── base.py
│   │   │   │   ├── yfinance_adapter.py
│   │   │   │   ├── akshare_adapter.py
│   │   │   │   ├── alphavantage_adapter.py
│   │   │   │   ├── binance_adapter.py
│   │   │   │   └── tushare_adapter.py
│   │   │   ├── factory.py             #     适配器工厂（智能路由）
│   │   │   ├── cache.py               #     Redis 缓存管理
│   │   │   └── models.py              #     Pydantic 统一数据模型
│   │   ├── schemas/                   #   API 响应信封
│   │   └── core/                      #   配置 / 异常 / 中间件
│   │       ├── config.py
│   │       ├── exceptions.py
│   │       └── middleware.py
│   ├── tests/
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
│
├── docker-compose.yml                 # 一键编排
├── ARCHITECTURE.md                    # 架构设计文档
└── README.md                          # 本文件
```

---

## 🚦 快速开始

### 环境要求
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose

### 方式一：Docker 一键启动（推荐）
```bash
git clone https://github.com/yourusername/KunLun_Terminal-Pro.git
cd KunLun_Terminal-Pro
docker-compose up --build
```
访问 `http://localhost:5173`

### 方式二：开发模式
```bash
# 终端 1 — 后端
cd backend
pip install -r requirements.txt
cp .env.example .env        # 填入你的 API Keys
python main.py               # → http://localhost:8000/docs

# 终端 2 — 前端
cd frontend
npm install
npm run dev                  # → http://localhost:5173
```

---

## 🗺️ 发展蓝图

| 阶段 | 内容 | 状态 |
| :--- | :--- | :---: |
| **Phase 1** | 核心框架 + 全球看板 + 大盘云图 | 🚧 |
| **Phase 2** | 个股 72 维诊断 + 贪恐/动量情绪引擎 | 📅 |
| **Phase 3** | AI 新闻因子工厂 + VectorBT 策略实验室 | 📅 |
| **Phase 4** | WebSocket 实时推送 + 移动端适配 | 💡 |

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request。请参阅 [ARCHITECTURE.md](./ARCHITECTURE.md) 了解设计规范。

## 📄 许可证

MIT License
