"""
YFinance Adapter — US stocks, global indices, crypto via Yahoo Finance.
"""
from typing import Any, Dict, List
import pandas as pd
from .base import BaseDataAdapter


class YFinanceAdapter(BaseDataAdapter):
    name = "yfinance"
    priority = 1
    supported_markets = ["us", "hk", "crypto", "index"]

    async def get_quote(self, ticker: str) -> Dict[str, Any]:
        # TODO: Implement with yfinance library
        raise NotImplementedError

    async def get_klines(
        self, ticker: str, interval: str = "1d", limit: int = 100
    ) -> pd.DataFrame:
        # TODO: Implement with yfinance.download()
        raise NotImplementedError

    async def get_index_members(self, index: str) -> List[Dict[str, Any]]:
        # TODO: Implement for S&P 500, DJIA, NASDAQ-100
        raise NotImplementedError

    async def search_ticker(self, query: str) -> List[Dict[str, str]]:
        # TODO: Implement ticker search
        raise NotImplementedError
