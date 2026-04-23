"""
KunLun Terminal Pro — Unified Data Models (Pydantic)
Canonical representations shared across all adapters and services.
"""
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# ─── Market / Index ───────────────────────────────────────
class QuoteModel(BaseModel):
    ticker: str
    name: str
    price: float
    change: float
    change_pct: float
    volume: float
    market: str            # us / cn / hk / crypto
    source: str            # yfinance / akshare / ...
    timestamp: datetime


class KlineBar(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


# ─── Cloud Map (Tree Map) ────────────────────────────────
class CloudMapItem(BaseModel):
    ticker: str
    name: str
    sector: str
    industry: str
    market_cap: float
    change_pct: float


class CloudMapData(BaseModel):
    market: str
    items: List[CloudMapItem]
    updated_at: datetime


# ─── Stock Analyzer (72-dim) ─────────────────────────────
class StockDiagnosis(BaseModel):
    ticker: str
    name: str
    # Scores
    fundamental_score: float       # 0-100
    technical_score: float         # 0-100
    sentiment_score: float         # 0-100
    total_score: float             # weighted composite
    rating: str                    # S / A / B / C / D
    # Key metrics
    market_cap: Optional[float] = None
    pe_ratio: Optional[float] = None
    pb_ratio: Optional[float] = None
    roe: Optional[float] = None
    fcf: Optional[float] = None
    beta: Optional[float] = None
    dividend_yield: Optional[float] = None


# ─── Sentiment ───────────────────────────────────────────
class FearGreedIndex(BaseModel):
    value: int             # 0-100
    label: str             # Extreme Fear / Fear / Neutral / Greed / Extreme Greed
    previous_close: int
    one_week_ago: int
    one_month_ago: int
    one_year_ago: int
    updated_at: datetime


class MomentumIndicator(BaseModel):
    index_name: str
    rsi_14: float
    macd: float
    macd_signal: float
    sma_50: float
    sma_200: float
    is_overbought: bool
    is_oversold: bool


# ─── News & Factor ───────────────────────────────────────
class NewsArticle(BaseModel):
    title: str
    source: str
    url: str
    published_at: datetime
    summary: Optional[str] = None
    sentiment: Optional[str] = None        # positive / negative / neutral
    sentiment_score: Optional[float] = None
    related_tickers: List[str] = []
    keywords: List[str] = []


class NewsFactor(BaseModel):
    keyword: str
    frequency: int
    avg_sentiment: float
    related_tickers: List[str]
    generated_at: datetime


# ─── Strategy / Backtest ─────────────────────────────────
class BacktestRequest(BaseModel):
    strategy_code: str
    ticker: str
    start_date: str
    end_date: str
    initial_capital: float = 100000.0
    commission: float = 0.001
    slippage: float = 0.001


class BacktestResult(BaseModel):
    total_return: float
    annual_return: float
    sharpe_ratio: float
    max_drawdown: float
    win_rate: float
    total_trades: int
    equity_curve: List[float]
    trade_log: List[dict]
