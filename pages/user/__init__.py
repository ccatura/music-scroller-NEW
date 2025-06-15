from flask import Blueprint, render_template

#this is wear we name the blueprint and tell flask where to find the templates
user_bp = Blueprint('user', __name__, template_folder='templates')

@user_bp.route('/user') #this is the route we will see this template on
def user():
    return render_template('user.html', title="User")