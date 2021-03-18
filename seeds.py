from app.models import User
from app.db import Session, Base, engine

#  drop and rebuild tables

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
    User(username='monty', email='nwestnedge0@cbc.ca', password='password123'),
    User(username='jakefromstateform', email='rmebes1@sogou.com', password='password123'),
    User(username='hoybaby', email='cstoneman2@last.fm', password='password123'),
    User(username='mchammer', email='ihellier3@goo.ne.jp', password='password123'),
    User(username='test123', email='gmidgley4@weather.com', password='password123')
])

db.commit()

db.close()