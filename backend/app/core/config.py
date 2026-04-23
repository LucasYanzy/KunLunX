"""
KunLun Terminal Pro — Global Configuration
Uses Pydantic Settings for type-safe environment variable management.
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # ─── App ──────────────────────────────────────────────
    PROJECT_NAME: str = "KunLun Terminal Pro"
    VERSION: str = "2.0.0"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    # ─── Database ─────────────────────────────────────────
    DATABASE_URL: str = "sqlite:///./data/kunlun.db"
    REDIS_URL: str = "redis://localhost:6379/0"

    # ─── AI Keys ──────────────────────────────────────────
    ANTHROPIC_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None

    # ─── Market Data Keys ─────────────────────────────────
    ALPHA_VANTAGE_KEY: Optional[str] = None
    TUSHARE_TOKEN: Optional[str] = None

    # ─── Cache TTL (seconds) ──────────────────────────────
    CACHE_TTL_TICK: int = 5
    CACHE_TTL_KLINE_1M: int = 60
    CACHE_TTL_KLINE_1D: int = 3600
    CACHE_TTL_NEWS: int = 300

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
