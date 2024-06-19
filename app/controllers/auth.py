from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, UserOut, Token
from app.crud import get_user_by_email, create_user, authenticate_user
from app.utils import create_access_token, decode_access_token, verify_password 
from app.dependencies import OAuth2PasswordRequestFormEmail

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = create_user(db=db, user=user)
    access_token = create_access_token(data={"sub": new_user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": new_user.email,
        "firstname": new_user.firstname,
        "lastname": new_user.lastname
    }
@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestFormEmail = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": user.email,
        "firstname": user.firstname,
        "lastname": user.lastname
    }
