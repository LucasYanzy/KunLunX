"""
KunLun Terminal Pro — Custom Exception Classes
"""
from fastapi import HTTPException


class DataSourceError(HTTPException):
    """Raised when all data adapters fail to return data."""
    def __init__(self, detail: str = "All data sources unavailable"):
        super().__init__(status_code=503, detail=detail)


class TickerNotFoundError(HTTPException):
    """Raised when a ticker symbol cannot be resolved."""
    def __init__(self, ticker: str):
        super().__init__(status_code=404, detail=f"Ticker '{ticker}' not found")


class BacktestError(HTTPException):
    """Raised when a backtest execution fails."""
    def __init__(self, detail: str):
        super().__init__(status_code=422, detail=f"Backtest failed: {detail}")


class AIServiceError(HTTPException):
    """Raised when the AI service (Claude/OpenAI) is unreachable."""
    def __init__(self, detail: str = "AI service unavailable"):
        super().__init__(status_code=502, detail=detail)
