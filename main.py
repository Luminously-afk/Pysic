
import click
from tidal import api
from tidal import downloader
def print_name(name):
    print("""
    --------------------------------------------------
    PYSIC - A python-based music downloader from tidal
    --------------------------------------------------
    """)

@click.command()
@click.option("-title", help="Title of the song")
@click.option("-artist", default="", help="Artist of the song")
@click.option("-album", default="", help="Album of the song")
@click.option("-quality", default="LOSSLESS", help="Quality of the song. [LOW, HIGH, LOSSLESS, HI_RES, HI_RES_LOSSLESS]")
def main(title, artist, album, quality):
    print(f"Searching for {title} by {artist} from {album}")
    list_song = api.search_songs(title=title, artist=artist, album=album)
    print_search_results(list_song)
    selected = click.prompt("Select a song to download", type=int)
    try:
        selected_song = list_song[selected-1]
    except IndexError:
        print("Invalid selection")
        return
    selected_song = api.get_track_url(selected_song, quality)
    print(f"Downloading {selected_song.get_title()} by {selected_song.get_artist()}")
    downloader.Downloader().download_track(selected_song.get_track_url(), f"{selected_song.get_title()} - {selected_song.get_artist()}.mp3")


def print_search_results(list_song):
    for i, song in enumerate(list_song):
        print(f"{i+1}. {song.get_title()} - {song.get_album()}")

if __name__ == "__main__":
    print_name("Pysic")
    main()
