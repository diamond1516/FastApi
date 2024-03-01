from pydantic import BaseModel, Field, validator, ValidationError, constr
from typing import Optional
from fastapi import HTTPException, status
import re

from users.models import PATTERN


class SignUpModel(BaseModel):
    phone: str = Field('+998912324191', min_length=13, max_length=13)
    email: Optional[str] = Field(example='ahmadboyabdurahimov589@gamil.com')
    password: str = Field(example='<PASSWORD>', min_length=8)
    name: Optional[str] = Field(example='Ahmad')

    @validator('email')
    def validate_email(cls, v):
        if not re.match(PATTERN, v):
            raise HTTPException(detail="Email is not valid", status_code=status.HTTP_400_BAD_REQUEST)
        return v

    class Config:
        orm_mode = True
        # schema_extra = {
        #     'example': {
        #         'phone': '+55555555555',
        #         'email': 'ahmadboy@gamil.com',
        #         'password': '1111',
        #         'name': '<NAME>'
        #     }
        # }
