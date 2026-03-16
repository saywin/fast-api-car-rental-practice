import os
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Session
from dotenv import load_dotenv

load_dotenv()

async_engine = create_async_engine(os.getenv("DATABASE_URL"), echo=True)


class Base(DeclarativeBase):
    pass


SessionLocal = async_sessionmaker(bind=async_engine, expire_on_commit=False)


async def get_db():
    async with SessionLocal() as session:
        yield session



SessionDep = Annotated[AsyncSession, Depends(get_db)]
