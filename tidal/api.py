import requests
from .models import Track
from . import SEACH_API, TRACK_API


def search_songs(title, **metadata) -> [Track]:
    url = SEACH_API(title=title, **metadata)
    response = requests.get(url)
    data = response.json()
    def parse_track(track):
        for item in track:
            yield Track(
                title=item.get('title'),
                artist=item['artist']['name'],
                album=item['album']['title'],
                id=item.get('id')
            )
    return list(parse_track(data['items']))


def get_track_url(track: Track, quality) -> Track:
    url = TRACK_API(id=track.get_id(), quality=quality)
    response = requests.get(url)
    if response.status_code == 404:
        return get_track_url(track, "LOSSLESS")
    data = response.json()
    track.set_track_url(data[2]['OriginalTrackUrl'])
    track.set_quality(data[1]['audioQuality'])
    return track