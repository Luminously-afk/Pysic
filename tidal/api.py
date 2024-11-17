import requests
from .models import Track
from . import SEACH_API


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