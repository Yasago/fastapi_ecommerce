from collections.abc import AsyncGenerator
from typing import Any

from app.backend.db import async_session_maker


async def get_db() -> AsyncGenerator[Any, Any]:
    async with async_session_maker() as session:
        yield session
