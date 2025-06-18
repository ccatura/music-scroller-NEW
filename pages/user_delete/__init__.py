from flask          import Blueprint, render_template, current_app, redirect, url_for
from models.user    import User
from models.song    import Song
from app import db

user_delete_bp = Blueprint('user_delete', __name__, template_folder='templates')

@user_delete_bp.route('/user_delete/<int:user_id>')
def user_delete(user_id):
    user = User.query.get(user_id)
    songs = Song.query.filter_by(owner_id=user_id).all()

    if user:
        user = user.query.get_or_404(user_id)
        # Delete all songs associated with the user
        for song in songs:
            db.session.delete(song)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('home.home', user_id=current_app.config['temp_user_id']))

    else:
        return "Song not found", 404