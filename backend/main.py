"""
KunLun Terminal Pro — FastAPI Application Entry Point
Wires all module routers, middleware, and lifecycle events.
"""
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.middleware import RequestTimingMiddleware
from app.data.cache import cache

# API routers — one per module
from app.api.v1 import market, stock, sentiment, news, strategy

# ─── Logging ──────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("kunlun")


# ─── Lifecycle ────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info(f"🏔️ {settings.PROJECT_NAME} v{settings.VERSION} starting...")
    await cache.connect(settings.REDIS_URL)
    logger.info("All systems online.")
    yield
    # Shutdown
    await cache.close()
    logger.info("Shutdown complete.")


# ─── App ──────────────────────────────────────────────────
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestTimingMiddleware)

# ─── Register Module Routers ─────────────────────────────
PREFIX = settings.API_V1_STR

app.include_router(market.router,    prefix=f"{PREFIX}/market",    tags=["Global Dashboard"])
app.include_router(stock.router,     prefix=f"{PREFIX}/stock",     tags=["Stock Analyzer"])
app.include_router(sentiment.router, prefix=f"{PREFIX}/sentiment", tags=["Sentiment"])
app.include_router(news.router,      prefix=f"{PREFIX}/news",      tags=["News Factory"])
app.include_router(strategy.router,  prefix=f"{PREFIX}/strategy",  tags=["Strategy Lab"])


@app.get("/")
async def root():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "docs": "/docs",
    }


# ─── Run ──────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
