from flask          import Blueprint, render_template
from models.user    import User
# from app import app

#this is wear we name the blueprint and tell flask where to find the templates
home_bp = Blueprint('home', __name__, template_folder='templates')

def get_users():
    return User.query.order_by(User.id).all()

@home_bp.route('/') #this is the route we will see this template on
def home():
    users = get_users()
    # temp_user_id = users[0].id
    # app.config['temp_user_id'] = temp_user_id
    return render_template('home.html', title="Home", data=users)

