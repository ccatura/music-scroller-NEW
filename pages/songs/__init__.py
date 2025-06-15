from flask          import Blueprint, render_template, request
from models.song    import Song
# from app            import db

songs_bp = Blueprint('songs', __name__, template_folder='templates')

def get_songs(sort_by="title"):
    if sort_by == "artist":
        return Song.query.order_by(Song.artist).all()
    elif sort_by == "date":
        return Song.query.order_by(Song.created_at.desc()).all()
    elif sort_by == "album":
        return Song.query.order_by(Song.album).all()
    else:
        return Song.query.order_by(Song.title).all()

@songs_bp.route('/songs')
def songs():
    sort = request.args.get("sort", "title")  # Default to "title"
    songs = get_songs(sort)
    song_quantity = len(songs)
    return render_template('songs.html', title="Songs", data=songs, song_quantity=song_quantity, current_sort=sort)