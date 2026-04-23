"""
KunLun API — Market Routes
Endpoints for global dashboard, cloud map, and kline data.
"""
from fastapi import APIRouter, Query
from app.services.market_service import market_service

router = APIRouter()


@router.get("/indices")
async def get_global_indices():
    """Get real-time quotes for major global indices."""
    data = await market_service.get_global_indices()
    return {"success": True, "data": data}


@router.get("/cloudmap/{market}")
async def get_cloud_map(market: str = "cn"):
    """
    Get tree-map data for a given market.
    Markets: cn (A-share), us, hk
    """
    data = await market_service.get_cloud_map(market)
    return {"success": True, "data": data}


@router.get("/klines/{ticker}")
async def get_klines(
    ticker: str,
    interval: str = Query("1d", description="1m / 5m / 15m / 1h / 1d / 1w"),
    limit: int = Query(100, ge=1, le=1000),
):
    """Get K-line (OHLCV) data for a ticker."""
    data = await market_service.get_klines(ticker, interval, limit)
    return {"success": True, "data": data}


@router.get("/search")
async def search_ticker(q: str = Query(..., min_length=1)):
    """Search tickers by name or code."""
    data = await market_service.search(q)
    return {"success": True, "data": data}
