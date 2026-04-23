"""
KunLun Terminal Pro — Middleware Stack
Logging, timing, and error handling middleware for FastAPI.
"""
import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("kunlun.middleware")


class RequestTimingMiddleware(BaseHTTPMiddleware):
    """Logs the processing time for every API request."""

    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        elapsed_ms = (time.perf_counter() - start) * 1000
        logger.info(
            f"{request.method} {request.url.path} — {response.status_code} — {elapsed_ms:.1f}ms"
        )
        return response
