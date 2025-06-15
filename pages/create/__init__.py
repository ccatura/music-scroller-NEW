from flask import Blueprint, render_template

#this is wear we name the blueprint and tell flask where to find the templates
create_bp = Blueprint('create', __name__, template_folder='templates')

@create_bp.route('/create') #this is the route we will see this template on
def create():
    return render_template('create.html', title="Create")