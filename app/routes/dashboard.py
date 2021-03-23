from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db

# this bp will be different url_prefix because i want it to go to dashboard html page
# once again, this file is a module so every variable or function that belongs to this module can be imported elsewhere.
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    db = get_db()
    posts = (   
        db.query(Post)
        .filter(Post.user_id == session.get('user_id'))
        .order_by(Post.created_at.desc())
        .all()
    )


    return render_template('dashboard.html')

@bp.route('./edit/<id>')
def edit(id):
    return render_template('edit-post.html')