from fastapi import APIRouter, Depends

from src.config import SessionDep
from src.dependencies import CarServiceDep
from src.models.cars import Car
from src.schemas.car_schemas import CarResponse, CarCreate, CarUpdate, CarFilter

car_router = APIRouter(prefix="/cars")


@car_router.get("/", response_model=list[CarResponse])
def get_cars(
    session: SessionDep,
    filter_car: CarFilter = Depends(),
) -> list[Car]:
    service = CarServiceDep
    return service.get_cars(session=session, filter_car=filter_car)


@car_router.get("/{car_id}", response_model=CarResponse)
def get_car(session: SessionDep, car_id: int) -> Car:
    service = CarServiceDep
    car = service.get_car(session=session, car_id=car_id)
    return car


@car_router.post("/", response_model=CarResponse)
def post_car(session: SessionDep, car: CarCreate) -> Car:
    service = CarServiceDep
    new_car = service.create_car(session=session, car=car)
    return new_car


@car_router.patch("/{car_id}", response_model=CarResponse)
def update_car(session: SessionDep, car_id: int, car: CarUpdate) -> Car:
    service = CarServiceDep
    car_by_id = get_car(session=session, car_id=car_id)
    changed_car = service.update_car(session=session, car=car, car_by_id=car_by_id)
    return changed_car

@car_router.delete("/{car_id}")
def delete_car(session: SessionDep, car_id: int) -> dict:
    service = CarServiceDep
    car_by_id = get_car(session=session, car_id=car_id)
    service.delete_car(session=session, car_by_id=car_by_id)
    return {"result": f"Car with id: {car_id} successful delete"}
