from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db


# Blueprint lets us consolidate routes into a dingle bp object and that the parent app can register later. Very similar to Router in express

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    # getting all posts
    db = get_db()
    # the get_db function return a sessiotn connects that tied to this route's context
    posts = db.query(Post).order_by(Post.created_at.desc()).all()

    return render_template('homepage.html', posts=posts)

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render single post template
    return render_template(
        'single-post.html',
        post=post
    )
    