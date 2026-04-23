

quant-terminal/
├── frontend/                 # Vue 3 前端（不变，仅移除模拟数据）
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── charts/       # 通用图表组件
│   │   │   ├── ui/           # UI组件
│   │   │   └── market/       # 市场专用组件
│   │   ├── layouts/
│   │   ├── modules/          # 业务模块（完全独立）
│   │   │   ├── global-dashboard/
│   │   │   ├── stock-analyzer/
│   │   │   ├── sentiment/
│   │   │   ├── news-factory/
│   │   │   └── strategy-lab/
│   │   ├── router/
│   │   ├── stores/           # Pinia状态管理（按模块拆分）
│   │   ├── types/            # 统一类型定义
│   │   ├── utils/
│   │   ├── api/              # 前端API调用层（按模块）
│   │   └── styles/
│   ├── package.json
│   └── vite.config.ts
├── backend/                  # FastAPI 后端（核心重构）
│   ├── app/
│   │   ├── api/              # API路由（按模块）
│   │   │   └── v1/
│   │   │       ├── market.py
│   │   │       ├── stock.py
│   │   │       ├── sentiment.py
│   │   │       ├── news.py
│   │   │       └── strategy.py
│   │   ├── core/             # 核心配置
│   │   │   ├── config.py
│   │   │   ├── exceptions.py
│   │   │   └── middleware.py
│   │   ├── data/             # 数据层（核心！多API适配器）
│   │   │   ├── adapters/     # 各API适配器（可插拔）
│   │   │   │   ├── base.py  # 抽象基类（必须继承）
│   │   │   │   ├── yfinance_adapter.py
│   │   │   │   ├── akshare_adapter.py
│   │   │   │   ├── alphavantage_adapter.py
│   │   │   │   ├── binance_adapter.py
│   │   │   │   └── tushare_adapter.py
│   │   │   ├── factory.py   # API工厂（自动选择最佳API）
│   │   │   ├── cache.py     # Redis缓存层
│   │   │   └── models.py    # 统一数据模型
│   │   ├── services/         # 业务逻辑层
│   │   │   ├── market_service.py
│   │   │   ├── stock_service.py
│   │   │   ├── sentiment_service.py
│   │   │   ├── news_service.py
│   │   │   └── strategy_service.py
│   │   ├── schemas/          # Pydantic响应模型
│   │   └── engines/          # 量化引擎（预留）
│   │       └── backtest.py
│   ├── data/                 # 本地数据存储
│   ├── tests/
│   ├── requirements.txt
│   ├── .env.example
│   └── main.py
├── docker/
├── docker-compose.yml
└── README.md