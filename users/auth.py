from fastapi import HTTPException, status, APIRouter, File, UploadFile
from . import models, schemas
from database import Session, engine
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path

from .utils import upload_file

Session = Session(bind=engine)

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.SignUpModel)
async def signup(user: schemas.SignUpModel):
    db_user = Session.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Wrong")
    new_user = models.User(
        email=user.email,
        phone=user.phone,
        name=user.name,
        password=generate_password_hash(user.password, method='pbkdf2:sha256')

    )
    Session.add(new_user)
    Session.commit()
    return new_user


@auth_router.post("/test", status_code=status.HTTP_201_CREATED)
async def test(file: UploadFile = File(...)):
    await upload_file(file)
    return {'msg': "salom"}
