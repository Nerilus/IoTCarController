from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas import UserCreate
from app.utils import get_password_hash
from app.utils.utils import verify_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        password=hashed_password,
        firstname=user.firstname,
        lastname=user.lastname,
        level_id=user.level_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user) 
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
# # CRUD operations for Level
# def get_level(db: Session, level_id: int):
#     return db.query(models.Level).filter(models.Level.id == level_id).first()

# def create_level(db: Session, level: schemas.LevelCreate):
#     db_level = models.Level(**level.dict())
#     db.add(db_level)
#     db.commit()
#     db.refresh(db_level)
#     return db_level

# # CRUD operations for Race
# def get_race(db: Session, race_id: int):
#     return db.query(models.Race).filter(models.Race.id == race_id).first()

# def create_race(db: Session, race: schemas.RaceCreate):
#     db_race = models.Race(**race.dict())
#     db.add(db_race)
#     db.commit()
#     db.refresh(db_race)
#     return db_race

# # CRUD operations for Lap
# def get_lap(db: Session, lap_id: int):
#     return db.query(models.Lap).filter(models.Lap.id == lap_id).first()

# def create_lap(db: Session, lap: schemas.LapCreate):
#     db_lap = models.Lap(**lap.dict())
#     db.add(db_lap)
#     db.commit()
#     db.refresh(db_lap)
#     return db_lap

# # CRUD operations for Metric
# def get_metric(db: Session, metric_id: int):
#     return db.query(models.Metric).filter(models.Metric.id == metric_id).first()

# def create_metric(db: Session, metric: schemas.MetricCreate):
#     db_metric = models.Metric(**metric.dict())
#     db.add(db_metric)
#     db.commit()
#     db.refresh(db_metric)
#     return db_metric
