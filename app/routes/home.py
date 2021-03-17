from flask import Blueprint, render_template

# Blueprint lets us consolidate routes into a dingle bp object and that the parent app can register later. Very similar to Router in express

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')

    