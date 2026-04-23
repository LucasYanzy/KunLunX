"""
KunLun API — News & Factor Routes
Endpoints for news feed, AI analysis, and factor generation.
"""
from fastapi import APIRouter, Query
from app.services.news_service import news_service

router = APIRouter()


@router.get("/latest")
async def get_latest_news(limit: int = Query(50, ge=1, le=200)):
    """Get latest financial news from all sources."""
    data = await news_service.fetch_latest(limit)
    return {"success": True, "data": data}


@router.get("/analyzed")
async def get_analyzed_news(limit: int = Query(20, ge=1, le=100)):
    """Get news enriched with AI sentiment analysis."""
    raw = await news_service.fetch_latest(limit)
    data = await news_service.analyze_sentiment(raw)
    return {"success": True, "data": data}


@router.get("/factors")
async def get_news_factors():
    """Get auto-generated news factors (keywords × sentiment)."""
    raw = await news_service.fetch_latest(100)
    analyzed = await news_service.analyze_sentiment(raw)
    factors = await news_service.generate_factors(analyzed)
    return {"success": True, "data": factors}


@router.get("/hot-keywords")
async def get_hot_keywords(hours: int = Query(24, ge=1, le=168)):
    """Get trending keywords in the last N hours."""
    data = await news_service.get_hot_keywords(hours)
    return {"success": True, "data": data}
