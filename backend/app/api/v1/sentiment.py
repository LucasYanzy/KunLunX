"""
KunLun API — Sentiment Routes
Endpoints for Fear & Greed, momentum, and VIX data.
"""
from fastapi import APIRouter, Query
from app.services.sentiment_service import sentiment_service

router = APIRouter()


@router.get("/fear-greed")
async def get_fear_greed():
    """Get current Fear & Greed Index value and label."""
    data = await sentiment_service.get_fear_greed()
    return {"success": True, "data": data}


@router.get("/fear-greed/history")
async def get_fear_greed_history(days: int = Query(30, ge=7, le=365)):
    """Get historical Fear & Greed values for charting."""
    data = await sentiment_service.get_fear_greed_history(days)
    return {"success": True, "data": data}


@router.get("/momentum/{index}")
async def get_momentum(index: str = "SPY"):
    """Get momentum indicators (RSI, MACD, SMA) for an index."""
    data = await sentiment_service.get_momentum(index)
    return {"success": True, "data": data}


@router.get("/vix")
async def get_vix():
    """Get current VIX level and recent history."""
    data = await sentiment_service.get_vix()
    return {"success": True, "data": data}
