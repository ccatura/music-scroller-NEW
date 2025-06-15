from flask          import Blueprint, render_template, request
from models.song    import Song
from app import app

songs_bp = Blueprint('songs', __name__, template_folder='templates')

def get_songs(sort_by="title", temp_user_id=None):
    if sort_by == "artist":
        # return Song.query.order_by(Song.artist).all()
        return Song.query.filter(Song.owner_id == temp_user_id).order_by(Song.artist).all()
    elif sort_by == "date":
        return Song.query.filter(Song.owner_id == temp_user_id).order_by(Song.created_at.desc()).all()
    elif sort_by == "album":
        return Song.query.filter(Song.owner_id == temp_user_id).order_by(Song.album).all()
    else:
        return Song.query.filter(Song.owner_id == temp_user_id).order_by(Song.title).all()

@songs_bp.route('/songs')
def songs():
    sort = request.args.get("sort", "title")  # Default to "title"
    temp_user_id = request.args.get("user_id", None)
    temp_username = request.args.get("username", None)
    songs = get_songs(sort, temp_user_id)
    song_quantity = len(songs)

    app.config['temp_user_id'] = temp_user_id
    app.config['temp_username'] = temp_username
    
    return render_template('songs.html',
                           title="Songs",
                           data=songs,
                           song_quantity=song_quantity,
                           current_sort=sort,
                           temp_user_id=temp_user_id,
                           temp_username=temp_username,
                           user_id=temp_user_id,
                           username=temp_username)