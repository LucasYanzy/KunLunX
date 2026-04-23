"""
KunLun API — Strategy Lab Routes
Endpoints for backtest execution, templates, and parameter optimization.
"""
from fastapi import APIRouter
from app.data.models import BacktestRequest
from app.services.strategy_service import strategy_service

router = APIRouter()


@router.post("/backtest")
async def run_backtest(request: BacktestRequest):
    """Execute a strategy backtest and return performance metrics."""
    result = await strategy_service.run_backtest(request)
    return {"success": True, "data": result}


@router.get("/templates")
async def list_templates():
    """List built-in strategy templates."""
    data = await strategy_service.list_templates()
    return {"success": True, "data": data}


@router.post("/optimize")
async def optimize_strategy(request: BacktestRequest, param_grid: dict = {}):
    """Grid-search parameter optimization for a strategy."""
    data = await strategy_service.optimize(request, param_grid)
    return {"success": True, "data": data}
