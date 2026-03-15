import enum
from decimal import Decimal

from sqlalchemy import String, Integer, DECIMAL, CheckConstraint, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.config import Base


class FuelTypeEnum(enum.Enum):
    GAS = "gas"
    DIESEL = "diesel"
    HYBRID = "hybrid"
    ELECTRIC = "electric"



class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    fuel_type: Mapped[FuelTypeEnum] = mapped_column(Enum(FuelTypeEnum), nullable=False)
    daily_rate: Mapped[Decimal] = mapped_column(DECIMAL(precision=6, scale=2), nullable=False)
    inventory: Mapped[int] = mapped_column(Integer, CheckConstraint("inventory > 0", name="check_positive_inventory"))

    def __str__(self):
        return f"Brand: {self.brand}, model: {self.model}, year: {self.year}"
