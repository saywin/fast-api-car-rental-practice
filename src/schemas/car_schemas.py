from decimal import Decimal

from pydantic import BaseModel, Field

from src.models.cars import FuelTypeEnum


class CarBase(BaseModel):
    brand: str = Field(max_length=255)
    model: str = Field(max_length=255)
    year: int = Field(gt=1990)
    fuel_type: FuelTypeEnum
    daily_rate: Decimal = Field(max_digits=6, decimal_places=2)
    inventory: int = Field(ge=0)


class CarResponse(CarBase):
    id: int


class CarCreate(CarBase):
    pass


class CarUpdate(BaseModel):
    brand: str | None = Field(max_length=255, default=None)
    model: str | None = Field(max_length=255, default=None)
    year: int | None = Field(gt=1900, default=None)
    fuel_type: FuelTypeEnum | None = Field(default=None)
    daily_rate: Decimal | None = Field(max_digits=6, decimal_places=2, default=None)
    inventory: int | None = Field(ge=0, default=None)


class CarFilter(BaseModel):
    brand: str | None = Field(default=None)
    model: str | None = Field(default=None)
    fuel_type: FuelTypeEnum | None = Field(default=None)
    max_year: int | None = Field(gt=1900, default=None)
    min_year: int | None = Field(gt=1900, default=None)
