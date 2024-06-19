from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    lastname: str
    firstname: str
    level_id: int

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    email: str
    firstname: str
    lastname: str

class TokenData(BaseModel):
    email: str

class LevelBase(BaseModel):
    level_name: str
    description: str = None
    max_speed: float = None

class LevelCreate(LevelBase):
    pass

class Level(LevelBase):
    id: int

    class Config:
        orm_mode = True

class RaceBase(BaseModel):
    name: str

class RaceCreate(RaceBase):
    pass

class Race(RaceBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class LapBase(BaseModel):
    time: str

class LapCreate(LapBase):
    pass

class Lap(LapBase):
    id: int
    race_id: int

    class Config:
        orm_mode = True

class MetricBase(BaseModel):
    pass

class MetricCreate(MetricBase):
    pass

class Metric(MetricBase):
    id: int
    race_id: int

    class Config:
        orm_mode = True
