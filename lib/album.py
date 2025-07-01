class Album:
    def __init__(self, id, title, release_year, artist_id, artist_name=''):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
        self.artist_name = artist_name
        
    def __eq__(self, other):
        # safer - checks same class first
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    def __str__(self):
        return f"* {self.id} - {self.title} ({self.release_year})"
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'artist_id': self.artist_id
        }