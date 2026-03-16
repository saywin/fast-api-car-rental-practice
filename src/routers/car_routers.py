from fastapi import APIRouter, Depends

from src.config import SessionDep
from src.dependencies import CarServiceDep
from src.models.cars import Car
from src.schemas.car_schemas import CarResponse, CarCreate, CarUpdate, CarFilter

car_router = APIRouter(prefix="/cars")


@car_router.get("/", response_model=list[CarResponse])
async def get_cars(
    session: SessionDep,
    filter_car: CarFilter = Depends(),
) -> list[Car]:
    service = CarServiceDep
    cars = await service.get_cars(session=session, filter_car=filter_car)
    return cars


@car_router.get("/{car_id}", response_model=CarResponse)
async def get_car(session: SessionDep, car_id: int) -> Car:
    service = CarServiceDep
    car = await service.get_car(session=session, car_id=car_id)
    return car


@car_router.post("/", response_model=CarResponse)
async def post_car(session: SessionDep, car: CarCreate) -> Car:
    service = CarServiceDep
    new_car = await service.create_car(session=session, car=car)
    return new_car


@car_router.patch("/{car_id}", response_model=CarResponse)
async def update_car(session: SessionDep, car_id: int, car: CarUpdate) -> Car:
    service = CarServiceDep
    car_by_id = await get_car(session=session, car_id=car_id)
    changed_car = await service.update_car(session=session, car=car, car_by_id=car_by_id)
    return changed_car

@car_router.delete("/{car_id}")
async def delete_car(session: SessionDep, car_id: int) -> dict:
    service = CarServiceDep
    car_by_id = await get_car(session=session, car_id=car_id)
    await service.delete_car(session=session, car_by_id=car_by_id)
    return {"result": f"Car with id: {car_id} successful delete"}
