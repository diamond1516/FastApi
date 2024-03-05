from pydantic import BaseModel, Field, validator
import typing


class CreateProductSchema(BaseModel):
    pass


class CreateCategorySchema(BaseModel):
    title: str = Field(default='Salom', min_length=5)
    image: typing.Optional[str] = Field('salom')
