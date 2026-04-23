"""
KunLun API — Stock Analyzer Routes
Endpoints for 72-dimension diagnosis and financial data.
"""
from fastapi import APIRouter
from app.services.stock_service import stock_service

router = APIRouter()


@router.get("/diagnose/{ticker}")
async def diagnose_stock(ticker: str):
    """Run full 72-dim multi-factor diagnosis on a stock."""
    data = await stock_service.diagnose(ticker)
    return {"success": True, "data": data}


@router.get("/financials/{ticker}")
async def get_financials(ticker: str):
    """Get detailed financial statements for a stock."""
    data = await stock_service.get_financials(ticker)
    return {"success": True, "data": data}


@router.get("/peers/{ticker}")
async def get_peers(ticker: str):
    """Get comparable peer stocks in the same sector."""
    data = await stock_service.get_peers(ticker)
    return {"success": True, "data": data}
