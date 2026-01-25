from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from env import FILE_DB



async_engine = create_async_engine(f"sqlite+aiosqlite:///{FILE_DB}", echo=False, pool_size=20, pool_recycle=295)
Session = async_sessionmaker(bind=async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
