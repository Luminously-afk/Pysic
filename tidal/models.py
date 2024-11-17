class Track(object):
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.artist = kwargs.get('artist')
        self.album = kwargs.get('album')
        self.id = kwargs.get('id')
        self.quality = kwargs.get('quality', "LOSSLESS")
        self.track_url = kwargs.get('track_url', "")
        self.cover = kwargs.get('cover', "")
        self.lyrics = kwargs.get('lyrics', "")
        self.sync_lyrics = False

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

    def set_track_url(self, url):
        self.track_url = url

    def set_quality(self, quality):
        self.quality = quality

    def get_cover(self):
        return f"https://resources.tidal.com/images/{self.cover.replace("-", "/")}/1280x1280.jpg"

    def get_lyrics(self):
        return self.lyrics

    def set_lyrics(self, lyrics):
        self.lyrics = lyrics

    def set_sync_lyrics(self, is_sync):
        self.sync_lyrics = is_sync

    def is_sync_lyrics(self):
        return self.sync_lyrics