"""
KunLun Terminal Pro — API Response Schemas
Wraps data models with standard API envelope (status, data, message).
"""
from pydantic import BaseModel
from typing import Any, Generic, List, Optional, TypeVar

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """Standard API response envelope."""
    success: bool = True
    data: Optional[T] = None
    message: str = "ok"


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated response for list endpoints."""
    success: bool = True
    data: List[T] = []
    total: int = 0
    page: int = 1
    page_size: int = 20
    message: str = "ok"
