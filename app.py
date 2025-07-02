import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.artist import Artist
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     # We use `render_template` to send the user the file `emoji.html`
#     # But first, it gets processed to look for placeholders like {{ emoji }}
#     # These placeholders are replaced with the values we pass in as arguments
#     return render_template('emoji.html', emoji=':)')

# === previous challenge ===
# @app.route('/albums', methods=['GET'])
# def get_all_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     albums = repository.all()

#     album_dicts = [album.to_dict() for album in albums]
#     return jsonify(album_dicts)

# @app.route('/albums', methods=['POST'])
# def post_new_album():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     title = request.form.get('title')
#     release_year = request.form.get('release_year')
#     artist_id = request.form.get('artist_id')
#     album = Album(None, title, release_year, artist_id)
#     repository.create(album)
#     return "", 200

# === Challenge ===

# @app.route('/artists', methods=['GET'])
# def get_all_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artists = repository.all()
    
#     artist_dicts = [artist.to_dict() for artist in artists]
#     return jsonify(artist_dicts), 200

# @app.route('/artists', methods=['POST'])
# def post_new_artist():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     name = request.form.get('name')
#     genre = request.form.get('genre')
#     artist = Artist(None, name, genre)
#     repository.create(artist)
#     return "", 200

# === Albums ===

@app.route('/albums', methods=['GET'])
def get_albums_page():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)

@app.route('/albums/new', methods=['GET'])
def get_new_album_page():
    return render_template('album_form.html')

@app.route('/albums', methods=['POST'])
def create_album():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    # Get the fields from the request form
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    # Create a book object
    album = Album(None, title, release_year, artist_id)

    # Check for validity and if not valid, show the form again with errors
    if not album.is_valid():
        return render_template('album_form.html', album=album, errors=album.generate_errors()), 400

    # Save the book to the database
    album = repository.create(album)
    # Redirect to the book's show route to the user can see it
    return redirect(f"/albums/{album.id}")

@app.route('/albums/<id>', methods=['GET'])
def get_album_page(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find_with_artist(id)
    if album is None:
        return "Album not found", 404
    return render_template('album.html', album=album)

# ==== Artists

@app.route('/artists', methods=['GET'])
def get_artists_page():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists.html', artists=artists)

@app.route('/artists/<id>', methods=['GET'])
def get_artist_page(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artist.html', artist=artist)








# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
