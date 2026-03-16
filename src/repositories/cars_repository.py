from fastapi import Depends
from sqlalchemy import select

from src.config import SessionDep
from src.models.cars import Car
from src.schemas.car_schemas import CarCreate, CarUpdate, CarFilter


class CarRepositories:
    @staticmethod
    async def get_cars(session: SessionDep, filter_car: CarFilter = Depends()) -> list[Car]:
        stmt = select(Car)
        filters = []

        if filter_car.brand:
            filters.append(Car.brand == filter_car.brand)

        if filter_car.model:
            filters.append(Car.model == filter_car.model)

        if filter_car.max_year:
            filters.append(Car.year <= filter_car.max_year)

        if filter_car.min_year:
            filters.append(Car.year >= filter_car.min_year)

        if filters:
            stmt = stmt.where(*filters)

        cars = (await session.scalars(stmt)).all()
        return cars

    @staticmethod
    async def get_car(session: SessionDep,car_id: int) -> Car:
        car = await session.get(Car, car_id)
        return car

    @staticmethod
    async def create_car(session: SessionDep, car: CarCreate) -> Car:
        new_car = Car(**car.model_dump())
        session.add(new_car)

        try:
            await session.flush()
            await session.commit()
        except Exception:
            await session.rollback()
            raise

        return new_car

    @staticmethod
    async def update_car(session: SessionDep, car: CarUpdate, car_by_id: Car) -> Car:
        for key, value in car.model_dump(exclude_unset=True).items():
            setattr(car_by_id, key, value)

        session.add(car_by_id)

        try:
            await session.flush()
            await session.commit()
        except Exception:
            await session.rollback()
            raise

        return car_by_id

    @staticmethod
    async def delete_car(session: SessionDep, car_by_id: Car) -> None:
        try:
            await session.delete(car_by_id)
            await session.commit()
        except Exception:
            await session.rollback()
            raise
