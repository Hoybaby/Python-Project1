from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt
# created a User class that inherits from the Base Class
# the Base class variables helps us map the models to real MySQL tables which is key

salt = bcrypt.gensalt()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

# the @validates('') targets the value of the column i am targeting
# the assert is basically the required in the html part where it needs it to function the return
    @validates('email')
    def validate_email(self, key, email):
        # make sure email address contains a @ character
        assert '@' in email

        return email

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4

        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def verify_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )

        # the .checkpw() method is to compare the incoming password, the password paramter to the one saved to the user ojbect