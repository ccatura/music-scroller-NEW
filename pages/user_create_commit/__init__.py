from flask          import Blueprint, render_template, request, redirect, url_for
from models.user    import User
from app            import db  # Import db from the main app module
from datetime       import datetime

#this is wear we name the blueprint and tell flask where to find the templates
user_create_commit_bp = Blueprint('user_create_commit', __name__, template_folder='templates')

@user_create_commit_bp.route('/user_create_commit', methods=['GET', 'POST']) #this is the route we will see this template on
def user_create_commit():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        created_at = datetime.utcnow()
        updated_at = datetime.utcnow()

        user = User(
            username = username,
            email = email,
            password = password,
            created_at = created_at,
            updated_at = updated_at
        )
        
    db.session.add(user)
    db.session.commit()
    # return "User created!"
    return render_template('user_create_commit.html', title="Commit User", username=username, email=email, password=password, created_at=created_at, updated_at=updated_at)

