from playwright.sync_api import Page, expect

# === exercise tests ===
def test_get_albums_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")

    div_items = page.locator('div')

    expect(div_items).to_have_text([
        "Title: Doolittle Released: 1989 go to album",
        "Title: Surfer Rosa Released: 1988 go to album",
        "Title: Waterloo Released: 1974 go to album",
        "Title: Super Trouper Released: 1980 go to album",
        "Title: Bossanova Released: 1990 go to album",
        "Title: Lover Released: 2019 go to album",
        "Title: Folklore Released: 2020 go to album",
        "Title: I Put a Spell on You Released: 1965 go to album",
        "Title: Baltimore Released: 1978 go to album",
        "Title: Here Comes the Sun Released: 1971 go to album",
        "Title: Fodder on My Wings Released: 1982 go to album",
        "Title: Ring Ring Released: 1973 go to album"
    ])

# === challenge ===
# Test-drive and implement a route that returns the HTML content for a single album
def test_get_album_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/1")

    div_items = page.locator('div')

    expect(div_items).to_have_text([
        "Doolittle Release year: 1989 Artist: Pixies back to albums"
    ])

# Add a route GET /artists which returns an HTML page with the list of artists. This page should contain a link for each artist listed, linking to /artists/<id> where <id> needs to be the corresponding artist id.
def test_get_artists_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/artists")

    div_items = page.locator('div')
    
    expect(div_items).to_have_text([
        "Name: Pixies Genre: Rock go to artist",
        "Name: ABBA Genre: Pop go to artist",
        "Name: Taylor Swift Genre: Pop go to artist",
        "Name: Nina Simone Genre: Jazz go to artist"
    ])

# Add a route GET /artists/<id> which returns an HTML page showing details for a single artist.

def test_get_artist_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/artists/1")
    
    div_items = page.locator('div')
    
    expect(div_items).to_have_text([
        "Pixies Genre: Rock back to artists"
    ])