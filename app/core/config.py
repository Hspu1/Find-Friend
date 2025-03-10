from os import getenv
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)
from sqlalchemy.orm import DeclarativeBase


load_dotenv()
db_url = getenv("DB_URL")

engine = create_async_engine(db_url)
async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
