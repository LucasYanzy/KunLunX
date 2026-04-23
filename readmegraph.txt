graph TD
    root[quant-terminal] --> frontend[frontend]
    root --> backend[backend]
    root --> docker[docker]
    root --> docker-compose.yml
    root --> README.md

    %% 前端子图
    subgraph "前端模块 (Vue 3 + Vite)"
        frontend --> public[public]
        frontend --> src[src]
        frontend --> package.json
        frontend --> vite.config.ts
        
        src --> assets[assets]
        src --> components[components]
        src --> layouts[layouts]
        src --> modules[modules]
        src --> router[router]
        src --> stores[stores]
        src --> types[types]
        src --> utils[utils]
        src --> api[api]
        src --> styles[styles]
        
        components --> charts[charts 通用图表]
        components --> ui[ui 基础组件]
        components --> market[market 市场专用]
        
        modules --> global-dashboard[global-dashboard]
        modules --> stock-analyzer[stock-analyzer]
        modules --> sentiment[sentiment 情绪分析]
        modules --> news-factory[news-factory 新闻工厂]
        modules --> strategy-lab[strategy-lab 策略实验室]
    end

    %% 后端子图
    subgraph "后端模块 (FastAPI 核心重构)"
        backend --> app[app]
        backend --> data[data 本地存储]
        backend --> tests[tests]
        backend --> requirements.txt
        backend --> .env.example
        backend --> main.py
        
        app --> api[api 路由]
        app --> core[core 核心配置]
        app --> data-layer[data 数据层]
        app --> services[services 业务逻辑]
        app --> schemas[schemas Pydantic]
        app --> engines[engines 量化引擎]
        
        api --> v1[v1]
        v1 --> market.py
        v1 --> stock.py
        v1 --> sentiment.py
        v1 --> news.py
        v1 --> strategy.py
        
        core --> config.py
        core --> exceptions.py
        core --> middleware.py
        
        data-layer --> adapters[adapters API适配器]
        data-layer --> factory.py[factory.py API工厂]
        data-layer --> cache.py[cache.py Redis缓存]
        data-layer --> models.py[models.py 数据模型]
        
        adapters --> base.py[base.py 抽象基类]
        adapters --> yfinance_adapter.py
        adapters --> akshare_adapter.py
        adapters --> alphavantage_adapter.py
        adapters --> binance_adapter.py
        adapters --> tushare_adapter.py
        
        services --> market_service.py
        services --> stock_service.py
        services --> sentiment_service.py
        services --> news_service.py
        services --> strategy_service.py
        
        engines --> backtest.py[backtest.py 回测引擎]
    end

    %% 样式定义
    classDef folder fill:#e1f5fe,stroke:#01579b,stroke-width:2px,rx:5px
    classDef file fill:#f3e5f5,stroke:#4a148c,stroke-width:1px,rx:2px
    classDef coreModule fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px,rx:5px
    classDef adapterModule fill:#fff3e0,stroke:#e65100,stroke-width:1px,rx:2px

    %% 应用样式
    class root folder
    class frontend,backend,docker folder
    class app,src,components,modules,data-layer,services,api,core,engines coreModule
    class adapters,base.py,yfinance_adapter.py,akshare_adapter.py,alphavantage_adapter.py,binance_adapter.py,tushare_adapter.py adapterModule
    class public,layouts,router,stores,types,utils,api,styles,charts,ui,market,global-dashboard,stock-analyzer,sentiment,news-factory,strategy-lab folder
    class data,tests folder
    class package.json,vite.config.ts,requirements.txt,.env.example,main.py,market.py,stock.py,sentiment.py,news.py,strategy.py,config.py,exceptions.py,middleware.py,factory.py,cache.py,models.py,market_service.py,stock_service.py,sentiment_service.py,news_service.py,strategy_service.py,backtest.py file



    flowchart TD
    User[用户操作] --> Frontend[Vue3 前端模块]
    
    Frontend --> ApiRequest[前端 API 请求]
    ApiRequest --> FastAPI[FastAPI 路由 v1]
    
    FastAPI --> Service[对应业务服务<br/>market/stock/sentiment/...]
    Service --> DataFactory[数据工厂 Data Factory]
    
    DataFactory --> SelectAdapter[自动选择最优适配器]
    
    SelectAdapter --> Adapter1[akshare 适配器]
    SelectAdapter --> Adapter2[tushare 适配器]
    SelectAdapter --> Adapter3[腾讯云适配器]
    SelectAdapter --> Adapter4[binance 适配器]
    
    Adapter1 & Adapter2 & Adapter3 & Adapter4 --> RawData[原始市场数据]
    
    RawData --> Cache{Redis 缓存检查}
    Cache -->|命中| DirectReturn[直接返回缓存数据]
    Cache -->|未命中| FetchReal[拉取最新数据]
    
    FetchReal --> UnifiedModel[统一数据模型 Pydantic]
    UnifiedModel --> CacheWrite[写入 Redis 热缓存]
    
    DirectReturn & CacheWrite --> ServiceBack[返回至业务服务]
    ServiceBack --> ApiResponse[API JSON 响应]
    ApiResponse --> FrontendRender[前端图表/页面渲染]



    flowchart LR
    MarketSource[行情源 QMT / 腾讯云]
    MarketSource --> RealTimeAdapter[实时数据适配器]
    
    RealTimeAdapter --> EventBus[事件总线 Event Bus]
    
    EventBus --> Sub1[行情推送订阅<br/>Frontend WS]
    EventBus --> Sub2[情绪分析引擎<br/>Sentiment Service]
    EventBus --> Sub3[策略计算引擎<br/>Strategy Lab]
    EventBus --> Sub4[资金流向监控]
    
    Sub3 --> Signal[交易信号 ORDER_SIGNAL]
    Signal --> TradeService[交易服务 QMT/XTP]
    TradeService --> OrderExec[订单执行/模拟下单]
    OrderExec --> ResultEvent[订单状态事件]
    
    ResultEvent --> EventBus
    EventBus --> FrontendNotify[前端弹窗/通知更新]



    flowchart TD
    subgraph 前端展示层
        FE[Vue3 模块]
    end
    
    subgraph 接口网关层
        API[FastAPI v1 路由]
    end
    
    subgraph 业务逻辑层
        SVC[Service 业务服务]
    end
    
    subgraph 数据核心层
        FACT[数据工厂]
        ADAPTER[多数据源适配器]
        CACHE[Redis 缓存]
    end
    
    subgraph 外部数据源
        EXT[腾讯云 / QMT / A 股 / 加密货币]
    end
    
    FE --> API
    API --> SVC
    SVC --> FACT
    FACT --> ADAPTER
    FACT --> CACHE
    ADAPTER --> EXT
    EXT --> ADAPTER