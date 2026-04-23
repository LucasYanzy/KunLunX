"""
KunLun Terminal Pro — Data Adapter Factory
Manages adapter registration, health-checks, and smart routing by market type.
"""
import asyncio
import logging
from typing import Dict, List, Optional, Type

from .adapters.base import BaseDataAdapter
from .adapters.yfinance_adapter import YFinanceAdapter
from .adapters.akshare_adapter import AkShareAdapter
from .adapters.alphavantage_adapter import AlphaVantageAdapter
from .adapters.binance_adapter import BinanceAdapter
from .adapters.tushare_adapter import TushareAdapter

logger = logging.getLogger("kunlun.data.factory")


class DataAdapterFactory:
    """
    Singleton factory: registers all adapters, groups them by market,
    performs health-checks, and returns the best available adapter.
    """

    def __init__(self):
        self._all: List[BaseDataAdapter] = []
        self._by_market: Dict[str, List[BaseDataAdapter]] = {}
        self._register_defaults()

    # ── Registration ────────────────────────────────────────
    def _register_defaults(self):
        adapter_classes: List[Type[BaseDataAdapter]] = [
            YFinanceAdapter,
            AkShareAdapter,
            AlphaVantageAdapter,
            BinanceAdapter,
            TushareAdapter,
        ]
        for cls in adapter_classes:
            try:
                instance = cls()
                self._all.append(instance)
            except Exception as e:
                logger.warning(f"Skip adapter {cls.name}: {e}")

        self._all.sort(key=lambda a: a.priority)
        self._rebuild_market_index()

    def _rebuild_market_index(self):
        markets = {"us", "cn", "hk", "crypto", "forex", "futures", "index"}
        self._by_market = {
            m: [a for a in self._all if m in a.supported_markets]
            for m in markets
        }

    # ── Health ──────────────────────────────────────────────
    async def refresh_health(self):
        results = await asyncio.gather(
            *(a.health_check() for a in self._all), return_exceptions=True
        )
        for adapter, ok in zip(self._all, results):
            if isinstance(ok, Exception) or not ok:
                logger.warning(f"Adapter {adapter.name} unhealthy")

    # ── Access ──────────────────────────────────────────────
    def get_best(self, market: str) -> Optional[BaseDataAdapter]:
        candidates = self._by_market.get(market, [])
        return candidates[0] if candidates else None

    def get_all(self, market: str) -> List[BaseDataAdapter]:
        return self._by_market.get(market, [])


# Global singleton
data_factory = DataAdapterFactory()
