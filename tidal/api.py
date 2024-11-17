import requests
from .models import Track
from . import SEACH_API, TRACK_API
import time

def search_songs(title, **metadata) -> [Track]:
    url = SEACH_API(title=title, **metadata)
    response = requests.get(url)
    if response.status_code != 200:
        time.sleep(3)
        return search_songs(title, **metadata)
    data = response.json()
    def parse_track(track):
        for item in track:
            yield Track(
                title=item.get('title'),
                artist=item['artist']['name'],
                album=item['album']['title'],
                id=item.get('id'),
                cover=item['album']['cover'],
            )
    return list(parse_track(data['items']))


def get_track_url(track: Track, quality) -> Track:
    url = TRACK_API(id=track.get_id(), quality=quality)
    response = requests.get(url)
    if response.status_code == 404:
        return get_track_url(track, "HIGH")
    elif response.status_code != 200:
        time.sleep(3)
        return get_track_url(track, quality)
    data = response.json()
    track.set_track_url(data[2]['OriginalTrackUrl'])
    track.set_quality(data[1]['audioQuality'])
    return track


def get_lyics(track: Track) -> Track:
    response = requests.get(f"https://tidal.401658.xyz/lyrics/?id={track.get_id()}")
    if response.status_code != 200:
        time.sleep(3)
        return get_lyics(track)
    data = response.json()
    if data[0]['subtitles'] == '':
        track.set_sync_lyrics(False)
        track.set_lyrics(data[0]['lyrics'])
        return track
    track.set_sync_lyrics(True)
    track.set_lyrics(data[0]['subtitles'])
    return track