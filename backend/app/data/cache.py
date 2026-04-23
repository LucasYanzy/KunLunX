"""
KunLun Terminal Pro — Redis Cache Layer
Wraps Redis with typed get/set helpers and configurable TTL.
"""
import json
import logging
from typing import Any, Optional

logger = logging.getLogger("kunlun.data.cache")


class CacheManager:
    """
    Async Redis cache wrapper.
    Initialised lazily — call `await cache.connect()` on app startup.
    """

    def __init__(self):
        self._redis = None

    async def connect(self, redis_url: str = "redis://localhost:6379/0"):
        try:
            import redis.asyncio as aioredis
            self._redis = aioredis.from_url(redis_url, decode_responses=True)
            await self._redis.ping()
            logger.info("Redis connected.")
        except Exception as e:
            logger.warning(f"Redis unavailable, running without cache: {e}")
            self._redis = None

    async def get(self, key: str) -> Optional[Any]:
        if not self._redis:
            return None
        raw = await self._redis.get(key)
        return json.loads(raw) if raw else None

    async def set(self, key: str, value: Any, ttl: int = 60):
        if not self._redis:
            return
        await self._redis.set(key, json.dumps(value, default=str), ex=ttl)

    async def delete(self, key: str):
        if self._redis:
            await self._redis.delete(key)

    async def close(self):
        if self._redis:
            await self._redis.close()


# Global singleton
cache = CacheManager()
