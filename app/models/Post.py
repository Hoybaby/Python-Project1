from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, datetime
from sqlalchemy.orm import relationship

# just like the user.py class to make a model properly for the table, need to make a python class.

class Post(base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)