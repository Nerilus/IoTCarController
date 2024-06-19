from pydantic import BaseModel

class SensorData(BaseModel):
    distance: float
    light: float 