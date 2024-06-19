from sqlalchemy import Column, Integer, String, ForeignKey, Float, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    level_id = Column(Integer, ForeignKey('levels.id'))

class Level(Base):
    __tablename__ = "levels"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    level_name = Column(String, index=True)
    description = Column(String, index=True)
    max_speed = Column(Float)

class Race(Base):
    __tablename__ = "race"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

class Lap(Base):
    __tablename__ = "lap"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    race_id = Column(Integer, ForeignKey('race.id'))
    time = Column(String)

class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    race_id = Column(Integer, ForeignKey('race.id'))

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    distance = Column(Float, nullable=False)
    light = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.now())