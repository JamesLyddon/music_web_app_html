import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.artist import Artist
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository

app = Flask(__name__)

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

@app.route('/artists/new', methods=['GET'])
def get_new_artist_page():
    return render_template('artist_form.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    name = request.form.get('name')
    genre = request.form.get('genre')
    
    artist = Artist(None, name, genre)
    
    # Check for validity and if not valid, show the form again with errors
    if not artist.is_valid():
        return render_template('artist_form.html', artist=artist, errors=artist.generate_errors()), 400

    artist = repository.create(artist)
    
    return redirect(f'/artists/{artist.id}')



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
