from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

# just like the user.py class to make a model properly for the table, need to make a python class.

class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now, onupdate=datetime.now)
    

    user = relationship('User')
    
    # In the SQLAlchemy model, we can define dynamic properties that won't become part of the MySQL table but that the query will return.

    comments = relationship('Comment', cascade='all,delete')
    # line 21 is so that if a post gets deleted, all the comments get deleted too

    vote_count = column_property(
        select([func.count(Vote.id)]).where(Vote.post_id == id)
    )
    # When we query the model, this dynamic property(column_property) will perform a SELECT, together with the SQLAlchemy func.count() method, to add up the votes.