from app.db import Base
from sqlalchemy import Column, Integer, String


# created a User class that inherits from the Base Class
# the Base class variables helps us map the models to real MySQL tables which is key


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)