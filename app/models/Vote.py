from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Vote(Base):
    __table__name: 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.is'))

# establish table refernce  

# user = relationship('User')