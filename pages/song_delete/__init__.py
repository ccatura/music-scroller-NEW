from flask          import Blueprint, render_template, current_app, redirect, url_for, flash
from models.song    import Song
from app import db

song_delete_bp = Blueprint('song_delete', __name__, template_folder='templates')

@song_delete_bp.route('/song_delete/<int:song_id>')
def song_delete(song_id):
    song = Song.query.get(song_id)
    if song:
        song = Song.query.get_or_404(song_id)
        db.session.delete(song)
        db.session.commit()
        return redirect(url_for('songs.songs', user_id=current_app.config['temp_user_id'], username=current_app.config['temp_username']))

    else:
        return "Song not found", 404