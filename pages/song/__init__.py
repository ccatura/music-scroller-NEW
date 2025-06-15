from flask          import Blueprint, render_template
from models.song    import Song

song_bp = Blueprint('song', __name__, template_folder='templates')

@song_bp.route('/song/<int:song_id>')
def show_song(song_id):
    song = Song.query.get(song_id)
    if song:
        return render_template('song.html', song=song)
    else:
        return "Song not found", 404