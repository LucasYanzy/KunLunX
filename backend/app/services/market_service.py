"""
KunLun — Market Service
Handles global indices, cloud map data, and real-time quotes.
"""
import logging
from typing import List, Optional
from app.data.factory import data_factory
from app.data.cache import cache
from app.data.models import QuoteModel, CloudMapData, KlineBar

logger = logging.getLogger("kunlun.service.market")


class MarketService:

    async def get_global_indices(self) -> List[QuoteModel]:
        """Fetch quotes for major global indices."""
        # TODO: fetch from best adapter, cache results
        raise NotImplementedError

    async def get_cloud_map(self, market: str = "cn") -> CloudMapData:
        """Build tree-map data grouped by sector for a given market."""
        # TODO: get index members, enrich with change_pct, return CloudMapData
        raise NotImplementedError

    async def get_klines(
        self, ticker: str, interval: str = "1d", limit: int = 100
    ) -> List[KlineBar]:
        """Fetch K-line data with cache-through pattern."""
        # TODO: check cache -> adapter -> cache set -> return
        raise NotImplementedError

    async def search(self, query: str) -> list:
        """Search tickers across all adapters."""
        raise NotImplementedError


market_service = MarketService()
