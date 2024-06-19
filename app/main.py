from fastapi import FastAPI
import os
from app.controllers import auth, sensor
from app.database import engine, Base

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(sensor.router, prefix="/v1", tags=["v1"])

