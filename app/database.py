from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


DATABASE_URL = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@db:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# DATABASE_URL = f"postgresql://{os.getenv('user')}:{os.getenv('password')}@db:{os.getenv('5432')}/{os.getenv('project_fil_rouge')}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
