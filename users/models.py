from database import Base, SessionLocal, engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
import re

PATTERN = re.compile(
    r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")


class BaseModel(Base):
    __abstract__ = True
    __tablename__ = "basemodel"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    phone = Column(String(25), unique=True)
    name = Column(String(255))
    email = Column(String(50), unique=True)
    password = Column(Text, nullable=True)
    profile = relationship("Profile", back_populates="user", uselist=False)
    age = Column(Integer)

    @validates("email")
    def validate_email(self, key, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email is not valid")
        return email


class Profile(BaseModel):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='profile')
    avatar = Column(String(255), nullable=True)
    bio = Column(Text, nullable=True)


class Token(BaseModel):
    __tablename__ = 'token'
    access_token = Column(String(100), unique=True)


class TestCategory(BaseModel):
    __tablename__ = 'test_category'
    avatar = Column(String)
    name = Column(String)
