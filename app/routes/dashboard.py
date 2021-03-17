from flask import Blueprint, render_template

# this bp will be different url_prefix because i want it to go to dashboard html page
# once again, this file is a module so every variable or function that belongs to this module can be imported elsewhere.
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    return render_template('dashboard.html')

@bp.route('./edit/<id>')
def edit(id):
    return render_template('edit-post.html')