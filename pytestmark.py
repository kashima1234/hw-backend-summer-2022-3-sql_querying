import datetime
import pytest
from sqlalchemy import Engine, text
from sql_queries import TASK_1_QUERY

pytestmark = pytest.mark.asyncio

async def test_query_1(engine: Engine) -> None:
    async with engine.connect() as conn:
        res = await conn.execute(text(TASK_1_QUERY))

    # Сравнение полученных результатов с ожидаемыми
    assert res.all() == [
        ("PG0235", datetime.timedelta(seconds=1500)),
        ("PG0234", datetime.timedelta(seconds=1500)),
        ("PG0233", datetime.timedelta(seconds=1500)),
        ("PG0235", datetime.timedelta(seconds=1500)),
        ("PG0234", datetime.timedelta(seconds=1500)),
    ]

