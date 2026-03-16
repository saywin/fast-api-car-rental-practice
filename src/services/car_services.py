from starlette.exceptions import HTTPException

from src.config import SessionDep
from src.models.cars import Car
from src.repositories.cars_repository import CarRepositories
from src.schemas.car_schemas import CarCreate, CarUpdate, CarFilter


class CarServices:
    def __init__(self, repositories: CarRepositories) -> None:
        self.repositories = repositories


    async def get_cars(self, session: SessionDep, filter_car: CarFilter):
        cars = await self.repositories.get_cars(session=session, filter_car=filter_car)
        return cars

    async def get_car(self, session: SessionDep, car_id: int):
        car = await self.repositories.get_car(session=session, car_id=car_id)

        if not car:
            raise HTTPException(status_code=404, detail="Car not found")

        return car

    async def create_car(self, session: SessionDep, car: CarCreate):
        new_car = await self.repositories.create_car(session=session, car=car)

        return new_car


    def update_car(self, session: SessionDep, car: CarUpdate, car_by_id: Car):
        changed_car = self.repositories.update_car(session=session, car=car, car_by_id=car_by_id)

        return changed_car

    def delete_car(self, session: SessionDep, car_by_id: Car) -> None:
        self.repositories.delete_car(session=session, car_by_id=car_by_id)
