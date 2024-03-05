from fastapi import HTTPException, status, APIRouter, File, UploadFile, Depends
import helpers
from . import models

from . import models, schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session as BaseSession


# SessionLocal = Session(bind=engine)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


common_router = APIRouter(
    prefix='/common'
)


# @common_router.post("create/product/", response_model=schemas.CreateProductSchema,
# status_code=status.HTTP_201_CREATED) async def create_product(product: schemas.CreateProductSchema, db: Session =
# Depends(SessionLocal)): return {"salom": "sa;p"}


@common_router.post("/create/category/", response_model=schemas.CreateCategorySchema,
                    status_code=status.HTTP_201_CREATED)
async def create_category(title: str, image: UploadFile = File(...), db: BaseSession = Depends(get_db)):
    image = await helpers.upload_file(image, 'category/')
    obj = models.Category(title=title, image=image)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return schemas.CreateCategorySchema(title=title, image=image)
