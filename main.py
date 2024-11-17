from tidal import api
from tidal import downloader
a  = api.search_songs("hello", artist="adele")

b = api.get_track_url(a[0], "LOSSLESS")
d = downloader.Downloader()

d.download_track(b.get_track_url(), "hello.mp3")