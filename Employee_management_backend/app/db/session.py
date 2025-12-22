from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import get_database_url

DATABASE_URL = get_database_url()

engine = create_async_engine(
    DATABASE_URL,
    pool_size = 5,
    max_overflow = 10,
    pool_pre_ping = True,
    echo = False,
    connect_args={
        "ssl": "require"
    }
)

asyncSessionLocal = async_sessionmaker(
    engine, 
    expire_on_commit = False
)