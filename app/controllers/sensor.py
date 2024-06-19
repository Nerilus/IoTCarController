from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.sensor import SensorData
from app.crud.sensor import create_sensor_data
from app.database import get_db


router = APIRouter()


@router.post("/sensor_data")
async def sensor_data(data: SensorData, db: Session = Depends(get_db)):
    db_sensor_data = create_sensor_data(db, data)
    if db_sensor_data:
        if data.distance < 30.0:
            stop_car()
        else:
            control_car_based_on_light(data.light)
        return{"status": 'success'}
    else:
        raise HTTPException(status_code=500, detail="Failed to save sensor data")

def stop_car():
    print("Obtacle detected.car stopped")

def control_car_based_on_light(light):
    print(f"Controlling car based on light level: {light}")    