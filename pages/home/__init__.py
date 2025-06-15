from flask import Blueprint, render_template

#this is wear we name the blueprint and tell flask where to find the templates
home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/') #this is the route we will see this template on
def home():
    return render_template('home.html', title="Home")

