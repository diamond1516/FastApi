from database import engine, Base
from users.models import User, Profile, BaseModel
Base.metadata.create_all(bind=engine)