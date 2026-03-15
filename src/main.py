from fastapi import FastAPI

from src.routers.car_routers import car_router

app = FastAPI()

app.include_router(car_router, tags=["Cars"])
