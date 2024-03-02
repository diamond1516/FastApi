from fastapi import HTTPException, status, APIRouter, File, UploadFile, Depends
import helpers

from . import models, schemas
from database import Session, engine

SessionLocal = Session(autocommit=False, bind=engine)
common_router = APIRouter(
    prefix='/common'
)


@common_router.post("/create/product/", response_model=schemas, status_code=status.HTTP_201_CREATED)
async def create_product(product: schemas.CreateProductSchema, db: Session = Depends(SessionLocal)):
    pass
