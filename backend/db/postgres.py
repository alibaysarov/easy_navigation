from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from config import settings

# url = (
#     f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_password}"
#     f"@localhost:{settings.db_port}/{settings.postgres_db}"
# )

url = settings.db_url

engine = create_async_engine(url)

engine = create_async_engine(url, echo=True)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
