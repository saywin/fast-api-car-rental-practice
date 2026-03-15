from datetime import datetime

from pydantic import EmailStr
from sqlalchemy import String, DATETIME, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.config import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[EmailStr] = mapped_column(String(200), index=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DATETIME(timezone=True), server_default=func.now())
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)

    def __str__(self):
        return self.email
