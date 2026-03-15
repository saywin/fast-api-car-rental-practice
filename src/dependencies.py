from src.repositories.cars_repository import CarRepositories
from src.services.car_services import CarServices

repository_car = CarRepositories()
CarServiceDep = CarServices(repository_car)
