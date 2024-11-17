import os
import click
import time
from tidal import api
from tidal import downloader
import os

def print_name():
    print("""
    --------------------------------------------------
    PYSIC - A python-based music downloader from tidal
    --------------------------------------------------
    """)


def main_menu():
    while True:
        os.system('cls')
        print_name()
        print("\n1. Search Song\n2. Exit")
        choice = click.prompt("Select an option", type=int)
        if choice == 1:
            search_song()
        elif choice == 2:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


def search_song():
    os.system('cls')
    title = click.prompt("Title of the song", type=str)
    artist = click.prompt("Artist of the song (optional)", default="", type=str)
    album = click.prompt("Album of the song (optional)", default="", type=str)

    print(f"Searching for {title} by {artist} from {album}")
    list_song = api.search_songs(title=title, artist=artist, album=album)

    if not list_song:
        print("No songs found. Returning to the menu in 3 seconds...")
        time.sleep(3)
        return

    print_search_results(list_song)
    selected = click.prompt("Select a song to download", type=int)
    try:
        selected_song = list_song[selected - 1]
    except IndexError:
        print("Invalid selection. Returning to the menu in 3 seconds...")
        time.sleep(3)
        return

    quality = click.prompt("Quality of the song. [LOW, HIGH, LOSSLESS, HI_RES, HI_RES_LOSSLESS] (Default: LOSSLESS)", default="LOSSLESS",
                           type=str)
    selected_song = api.get_track_url(selected_song, quality)
    print(f"Downloading {selected_song.get_title()} by {selected_song.get_artist()}")
    downloader.Downloader().download_track(selected_song.get_track_url(),
                                           f"{selected_song.get_title()} - {selected_song.get_artist()}.mp3")


def print_search_results(list_song):
    for i, song in enumerate(list_song):
        print(f"{i + 1}. {song.get_title()} - {song.get_album()}")


if __name__ == "__main__":
    main_menu()