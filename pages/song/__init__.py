from flask          import Blueprint, render_template, current_app
from models.song    import Song
from app import app

song_bp = Blueprint('song', __name__, template_folder='templates')

@song_bp.route('/song/<int:song_id>')
def show_song(song_id):
    song = Song.query.get(song_id)
    if song:
        temp_user_id = current_app.config['temp_user_id']
        temp_username = current_app.config['temp_username']
        return render_template('song.html', song=song, temp_user_id=temp_user_id, temp_username=temp_username)
    else:
        return "Song not found", 404