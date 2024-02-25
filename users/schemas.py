from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    phone: str
    email: Optional[str]
    password: str
    name: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'phone': '+55555555555',
                'email': 'ahmadboy@gamil.com',
                'password': '1111',
                'name': '<NAME>'
            }
        }
