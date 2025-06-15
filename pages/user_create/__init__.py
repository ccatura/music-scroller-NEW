from flask          import Blueprint, render_template
from models.user    import User
from app            import db  # Import db from the main app module
from datetime       import datetime

#this is wear we name the blueprint and tell flask where to find the templates
user_create_bp = Blueprint('user_create', __name__, template_folder='templates')

@user_create_bp.route('/user_create') #this is the route we will see this template on
def user_create():
    return render_template('user_create.html', title="Create User")

