from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    'postgresql+psycopg2://fastapi:fastapi@localhost:5432/fastapi',
    echo=True
)
Session = sessionmaker()
Base = declarative_base()

