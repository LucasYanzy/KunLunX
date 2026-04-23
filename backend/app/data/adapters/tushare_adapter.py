"""
Tushare Adapter — A-share professional-grade data via Tushare Pro.
"""
from typing import Any, Dict, List
import pandas as pd
from .base import BaseDataAdapter


class TushareAdapter(BaseDataAdapter):
    name = "tushare"
    priority = 2
    supported_markets = ["cn"]

    async def get_quote(self, ticker: str) -> Dict[str, Any]:
        # TODO: Implement with tushare pro API
        raise NotImplementedError

    async def get_klines(
        self, ticker: str, interval: str = "1d", limit: int = 100
    ) -> pd.DataFrame:
        raise NotImplementedError

    async def get_index_members(self, index: str) -> List[Dict[str, Any]]:
        raise NotImplementedError

    async def search_ticker(self, query: str) -> List[Dict[str, str]]:
        raise NotImplementedError
