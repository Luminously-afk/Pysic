from mutagen.mp3 import MP3
from mutagen.flac import FLAC, Picture
from mutagen.id3 import ID3,APIC, USLT, SYLT, Encoding
from .models import Track
from .api import get_lyics
import requests
import re
import json
def add_metadata(file_path, trac: Track):
    track = get_lyics(trac)
    if file_path.endswith(".mp3"):
        track = get_lyics(track)
        audio = MP3(file_path, ID3=ID3)
        audio["title"] = track.get_title()
        audio["artist"] = track.get_artist()
        audio["album"] = track.get_album()
        audio.tags.add()

        if track.is_sync_lyrics():
            parsed = parse_lyrics(track.get_lyrics())
            audio.tags.add(
                SYLT(encoding=Encoding.UTF8, lang='eng', format=2, type=1, text=parsed)
            )
        else:
            audio.tags.add(
                USLT(encoding=Encoding.UTF8, lang='eng', desc='', text=track.get_lyrics())
            )

        audio.tags.add(
            APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,
                desc='Cover',
                data=fetch_album_art(track.get_cover())
            )
        )
        audio.save()
    elif file_path.endswith(".flac"):
        audio = FLAC(file_path)
        audio["title"] = track.get_title()
        audio["artist"] = track.get_artist()
        audio["album"] = track.get_album()

        if track.is_sync_lyrics():
            parsed = parse_lyrics(track.get_lyrics())
            synced = [{"time": timestamp, "text": lyric} for timestamp, lyric in parsed]
            audio["SYNCED_LYRICS"] = json.dumps(synced)
        else:
            audio["LYRICS"] = track.get_lyrics()

        pic = Picture()
        pic.type = 3
        pic.mime = 'image/jpeg'
        pic.desc = 'Cover'
        pic.data = fetch_album_art(track.get_cover())

        audio.add_picture(pic)
        audio.save()


def fetch_album_art(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def parse_lyrics(lyrics):
    pattern = re.compile(r'\[(\d+):(\d+\.\d+)\] (.+)')
    parsed_lyrics = []

    for line in lyrics.split('\n'):
        match = pattern.match(line)
        if match:
            minutes = int(match.group(1))
            seconds = float(match.group(2))
            timestamp = int((minutes * 60 + seconds) * 1000)
            lyric = match.group(3)
            parsed_lyrics.append((timestamp, lyric))

    return parsed_lyrics