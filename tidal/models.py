class Track(object):
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.artist = kwargs.get('artist')
        self.album = kwargs.get('album')
        self.id = kwargs.get('id')
        self.quality = kwargs.get('quality', "LOSSLESS")
        self.track_url = kwargs.get('track_url', "")

    def __repr__(self):
        return f'{self.title} by {self.artist}'

    def __str__(self):
        return f'{self.title} by {self.artist}'

    #make a getters function not a property
    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_album(self):
        return self.album

    def get_id(self):
        return self.id

    def get_quality(self):
        return self.quality

    def get_track_url(self):
        return self.track_url