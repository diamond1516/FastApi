from pydantic import BaseModel, Field
from typing import Optional


class SignUpModel(BaseModel):
    phone: str = Field('+998912324191', min_length=13, max_length=13)
    email: Optional[str] = Field(example='ahmadboyabdurahimov589@gamil.com')
    password: str = Field(example='<PASSWORD>', min_length=8)
    name: Optional[str] = Field(example='Ahmad')

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
