from flask          import Blueprint, render_template, request, current_app
from models.song    import Song
from app            import db  # Import db from the main app module
from datetime       import datetime

#this is wear we name the blueprint and tell flask where to find the templates
song_create_commit_bp = Blueprint('song_create_commit', __name__, template_folder='templates')

@song_create_commit_bp.route('/song_create_commit', methods=['GET', 'POST']) #this is the route we will see this template on
def song_create_commit():
    if request.method == 'POST':
        title = request.form.get('title')
        subtitle = request.form.get('subtitle')
        artist = request.form.get('artist')
        album = request.form.get('album')
        genre = request.form.get('genre')
        year = request.form.get('year')
        lyrics = request.form.get('lyrics')
        created_at = datetime.utcnow()
        updated_at = datetime.utcnow()

        temp_user_id = current_app.config['temp_user_id']

        song = Song(
            title = title,
            subtitle = subtitle,
            artist = artist,
            album = album,
            genre = genre,
            year = year,
            lyrics = lyrics,
            owner_id = temp_user_id,
            created_at = created_at,
            updated_at = updated_at
        )
        
    db.session.add(song)
    db.session.commit()
    # return "Song created!"
    return render_template(
        'song_create_commit.html',
        page_title="Commit Song",
        title=title,
        subtitle=subtitle,
        artist=artist,
        album=album,
        genre=genre,
        year=year,
        lyrics=lyrics,
        owner_id=temp_user_id,
        created_at=created_at,
        updated_at=updated_at
        )

