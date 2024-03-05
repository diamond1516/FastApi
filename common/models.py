from database import Base, SessionLocal, engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True)
    image = Column(String(255), nullable=True)
    products = relationship('Product', back_populates='category')


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='products')

