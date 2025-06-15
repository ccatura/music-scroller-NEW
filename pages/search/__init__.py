from flask import Blueprint, render_template

#this is wear we name the blueprint and tell flask where to find the templates
search_bp = Blueprint('search', __name__, template_folder='templates')

@search_bp.route('/search') #this is the route we will see this template on
def search():
    return render_template('search.html', title="Search")