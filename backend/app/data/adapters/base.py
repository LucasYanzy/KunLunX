"""
KunLun Terminal Pro — Base Data Adapter (Abstract)
All data source adapters MUST inherit from this class.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import pandas as pd


class BaseDataAdapter(ABC):
    """
    Contract for all market data adapters.
    Subclasses: YFinanceAdapter, AkShareAdapter, BinanceAdapter, etc.
    """

    name: str = "base"
    priority: int = 99  # Lower = preferred
    supported_markets: List[str] = []

    @abstractmethod
    async def get_quote(self, ticker: str) -> Dict[str, Any]:
        """Get real-time quote for a single ticker."""
        ...

    @abstractmethod
    async def get_klines(
        self, ticker: str, interval: str = "1d", limit: int = 100
    ) -> pd.DataFrame:
        """Get historical K-line (OHLCV) data."""
        ...

    @abstractmethod
    async def get_index_members(self, index: str) -> List[Dict[str, Any]]:
        """Get constituent stocks of an index (for cloud map)."""
        ...

    @abstractmethod
    async def search_ticker(self, query: str) -> List[Dict[str, str]]:
        """Search for tickers by name or code."""
        ...

    async def health_check(self) -> bool:
        """Return True if the adapter is reachable. Override for custom logic."""
        return True
