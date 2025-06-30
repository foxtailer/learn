import asyncio

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine

from config import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10
)

with sync_engine.connect() as c:  # With connect ROLBACK after exit. With BEGIN - COMMIT
    result = c.execute(
        text(
            "SELECT VERSION()"
        )
    )

    print(result.all())


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10
)

async def get_query():
    async with async_engine.connect() as c:  # With connect ROLBACK after exit. With BEGIN - COMMIT
        result = await c.execute(
            text(
                "SELECT VERSION()"
            )
        )

        print(result.all())

asyncio.run(get_query())
