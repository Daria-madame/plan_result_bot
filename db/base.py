from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from env import FILE_DB

engine = create_async_engine(f"sqlite+aiosqlite:///{FILE_DB}")

Session = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass
