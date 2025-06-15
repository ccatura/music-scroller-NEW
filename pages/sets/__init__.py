from flask import Blueprint, render_template

#this is wear we name the blueprint and tell flask where to find the templates
sets_bp = Blueprint('sets', __name__, template_folder='templates')

@sets_bp.route('/sets') #this is the route we will see this template on
def sets():
    return render_template('sets.html', title="Sets")