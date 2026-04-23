"""
AkShare Adapter — A-share (CN), HK stock, futures, forex via AkShare (免费).
"""
from typing import Any, Dict, List
import pandas as pd
from .base import BaseDataAdapter


class AkShareAdapter(BaseDataAdapter):
    name = "akshare"
    priority = 2
    supported_markets = ["cn", "hk", "futures", "forex"]

    async def get_quote(self, ticker: str) -> Dict[str, Any]:
        # TODO: Implement with akshare
        raise NotImplementedError

    async def get_klines(
        self, ticker: str, interval: str = "1d", limit: int = 100
    ) -> pd.DataFrame:
        # TODO: Implement with akshare
        raise NotImplementedError

    async def get_index_members(self, index: str) -> List[Dict[str, Any]]:
        # TODO: Implement for 沪深300, 上证50, 中证500
        raise NotImplementedError

    async def search_ticker(self, query: str) -> List[Dict[str, str]]:
        # TODO: Implement ticker search
        raise NotImplementedError
