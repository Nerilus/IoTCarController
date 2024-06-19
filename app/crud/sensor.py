from sqlalchemy.orm import Session
from app.models.models import SensorData as SensorDataModel
from app.schemas.sensor import SensorData as SensorDataSchema

def create_sensor_data(db: Session, sensor_data: SensorDataSchema):
    db_sensor_data = SensorDataModel(distance=sensor_data.distance, light=sensor_data.light)
    db.add(db_sensor_data)
    db.commit()
    db.refresh(db_sensor_data)
    return db_sensor_data
