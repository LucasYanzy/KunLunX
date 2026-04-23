"""
Binance Adapter — Cryptocurrency spot & futures data via Binance API.
"""
from typing import Any, Dict, List
import pandas as pd
from .base import BaseDataAdapter


class BinanceAdapter(BaseDataAdapter):
    name = "binance"
    priority = 1
    supported_markets = ["crypto"]

    async def get_quote(self, ticker: str) -> Dict[str, Any]:
        # TODO: Implement with Binance REST / WebSocket
        raise NotImplementedError

    async def get_klines(
        self, ticker: str, interval: str = "1d", limit: int = 100
    ) -> pd.DataFrame:
        raise NotImplementedError

    async def get_index_members(self, index: str) -> List[Dict[str, Any]]:
        raise NotImplementedError

    async def search_ticker(self, query: str) -> List[Dict[str, str]]:
        raise NotImplementedError
