from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
# === Previous Challenge Test ===
# """
# GET /album
# gets all albums as json
# """
# def test_get_albums(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     response = web_client.get("/albums")
#     assert response.status_code == 200
#     assert response.get_json() == [
#         {
#             "id": 1,
#             "release_year": 1989,
#             "title": "Doolittle",
#             "artist_id": 1
#         },
#         {
#             "id": 2,
#             "release_year": 1988,
#             "title": "Surfer Rosa",
#             "artist_id": 1
#         },
#         {
#             "id": 3,
#             "release_year": 1974,
#             "title": "Waterloo",
#             "artist_id": 2
#         },
#         {
#             "id": 4,
#             "release_year": 1980,
#             "title": "Super Trouper",
#             "artist_id": 2
#         },
#         {
#             "id": 5,
#             "release_year": 1990,
#             "title": "Bossanova",
#             "artist_id": 1
#         },
#         {
#             "id": 6,
#             "release_year": 2019,
#             "title": "Lover",
#             "artist_id": 3
#         },
#         {
#             "id": 7,
#             "release_year": 2020,
#             "title": "Folklore",
#             "artist_id": 3
#         },
#         {
#             "id": 8,
#             "release_year": 1965,
#             "title": "I Put a Spell on You",
#             "artist_id": 4
#         },
#         {
#             "id": 9,
#             "release_year": 1978,
#             "title": "Baltimore",
#             "artist_id": 4
#         },
#         {
#             "id": 10,
#             "release_year": 1971,
#             "title": "Here Comes the Sun",
#             "artist_id": 4
#         },
#         {
#             "id": 11,
#             "release_year": 1982,
#             "title": "Fodder on My Wings",
#             "artist_id": 4
#         },
#         {
#             "id": 12,
#             "release_year": 1973,
#             "title": "Ring Ring",
#             "artist_id": 2
#         }
#     ]

# def test_add_album(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     response = web_client.post("/albums", data={'title':'Voyage', 'release_year':'2022', 'artist_id': '2'})
#     assert response.status_code == 200
#     response = web_client.get("/albums")
#     assert response.status_code == 200
#     assert response.get_json() == [
#         {
#             "id": 1,
#             "release_year": 1989,
#             "title": "Doolittle",
#             "artist_id": 1
#         },
#         {
#             "id": 2,
#             "release_year": 1988,
#             "title": "Surfer Rosa",
#             "artist_id": 1
#         },
#         {
#             "id": 3,
#             "release_year": 1974,
#             "title": "Waterloo",
#             "artist_id": 2
#         },
#         {
#             "id": 4,
#             "release_year": 1980,
#             "title": "Super Trouper",
#             "artist_id": 2
#         },
#         {
#             "id": 5,
#             "release_year": 1990,
#             "title": "Bossanova",
#             "artist_id": 1
#         },
#         {
#             "id": 6,
#             "release_year": 2019,
#             "title": "Lover",
#             "artist_id": 3
#         },
#         {
#             "id": 7,
#             "release_year": 2020,
#             "title": "Folklore",
#             "artist_id": 3
#         },
#         {
#             "id": 8,
#             "release_year": 1965,
#             "title": "I Put a Spell on You",
#             "artist_id": 4
#         },
#         {
#             "id": 9,
#             "release_year": 1978,
#             "title": "Baltimore",
#             "artist_id": 4
#         },
#         {
#             "id": 10,
#             "release_year": 1971,
#             "title": "Here Comes the Sun",
#             "artist_id": 4
#         },
#         {
#             "id": 11,
#             "release_year": 1982,
#             "title": "Fodder on My Wings",
#             "artist_id": 4
#         },
#         {
#             "id": 12,
#             "release_year": 1973,
#             "title": "Ring Ring",
#             "artist_id": 2
#         },
#         {
#             "id": 13,
#             "release_year": 2022,
#             "title": "Voyage",
#             "artist_id": 2
#         }
#     ]

# Request: GET /artists
# Expected response (200 OK) Pixies, ABBA, Taylor Swift, Nina Simone
def test_get_artists(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.get_json() == [
        {
            "id": 1,
            "name": "Pixies",
            "genre": "Rock"
        },
        {
            "id": 2,
            "name": "ABBA",
            "genre": "Pop"
        },
        {
            "id": 3,
            "name": "Taylor Swift",
            "genre": "Pop"
        },
        {
            "id": 4,
            "name": "Nina Simone",
            "genre": "Jazz"
        },
    ]

# Request: POST /artists
# With body parameters: name=Wild Nothing genre=Indie
# Expected response (200 OK) (No content)
# Then subsequent request: GET /artists
# Expected response (200 OK) Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
def test_add_artist(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/artists', data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.get_json() == [
        {
            "id": 1,
            "name": "Pixies",
            "genre": "Rock"
        },
        {
            "id": 2,
            "name": "ABBA",
            "genre": "Pop"
        },
        {
            "id": 3,
            "name": "Taylor Swift",
            "genre": "Pop"
        },
        {
            "id": 4,
            "name": "Nina Simone",
            "genre": "Jazz"
        },
        {
            "id": 5,
            "name": "Wild Nothing",
            "genre": "Indie"
        }
    ]

# === exercise tests ===
def test_get_albums_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")

    div_items = page.locator('div')

    expect(div_items).to_have_text([
        "Title: Doolittle Released: 1989",
        "Title: Surfer Rosa Released: 1988",
        "Title: Waterloo Released: 1974",
        "Title: Super Trouper Released: 1980",
        "Title: Bossanova Released: 1990",
        "Title: Lover Released: 2019",
        "Title: Folklore Released: 2020",
        "Title: I Put a Spell on You Released: 1965",
        "Title: Baltimore Released: 1978",
        "Title: Here Comes the Sun Released: 1971",
        "Title: Fodder on My Wings Released: 1982",
        "Title: Ring Ring Released: 1973",
    ])

# === chellenge ===
# Test-drive and implement a route that returns the HTML content for a single album
def test_get_album_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/1")

    div_items = page.locator('div')

    expect(div_items).to_have_text([
        "Doolittle Release year: 1989 Artist: Pixies"
    ])
