"""
KunLun — Strategy Service
Strategy management, code execution, and backtest orchestration.
"""
import logging
from app.data.models import BacktestRequest, BacktestResult

logger = logging.getLogger("kunlun.service.strategy")


class StrategyService:

    async def run_backtest(self, request: BacktestRequest) -> BacktestResult:
        """
        Execute a user-defined strategy via VectorBT Pro:
        1. Fetch historical data for the ticker
        2. Execute strategy_code in a sandboxed environment
        3. Compute performance metrics
        4. Return BacktestResult with equity curve + trade log
        """
        raise NotImplementedError

    async def list_templates(self) -> list:
        """
        Return built-in strategy templates:
        - SMA Crossover
        - RSI Mean Reversion
        - Momentum
        - Pairs Trading
        """
        raise NotImplementedError

    async def optimize(self, request: BacktestRequest, param_grid: dict) -> list:
        """
        Grid-search over parameter combinations and return
        sorted results by Sharpe ratio.
        """
        raise NotImplementedError


strategy_service = StrategyService()
