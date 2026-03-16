import os
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from dotenv import load_dotenv

load_dotenv()

async_engine = create_async_engine(os.getenv("DATABASE_URL"), echo=True)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(bind=async_engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


SessionDep = Annotated[Session, Depends(get_db)]
