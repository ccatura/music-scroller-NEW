from flask          import Blueprint, render_template, current_app
from models.user    import User
from app            import db  # Import db from the main app module
from datetime       import datetime

#this is wear we name the blueprint and tell flask where to find the templates
song_create_bp = Blueprint('song_create', __name__, template_folder='templates')

@song_create_bp.route('/song_create') #this is the route we will see this template on
def song_create():
    temp_user_id = current_app.config['temp_user_id']
    return render_template('song_create.html', title="Create Song", temp_user_id=temp_user_id)

