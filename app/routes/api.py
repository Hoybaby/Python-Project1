from flask import Blueprint, request
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

# we add a new route that will resole to /api/users and specified the method to be POST
# purpose of a POST route is to receive data but then using, request from flask to retrieve it
@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()

    # this data that we are getting is returning an object which we will pass into a new User model.

    newUser = User(
        username = data.username,
        email = data.email,
        password = data.password
    )

    # print(data)

    return ''