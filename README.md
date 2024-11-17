# Pysic

Welcome to Pysic! This is my very first project, and I'm just learning Python. This project is still in development.

## Overview

Pysic is a Python-based application that allows users to search for songs and download them with ease. The project leverages the Tidal API to fetch song information and provides a downloader with a progress bar to download tracks.

## Features

- **Search Songs**: Search for songs by title and artist.
- **Track Information**: Retrieve detailed information about tracks.
- **Download Tracks**: Download tracks with a progress bar to monitor the download status.

## Installation

To get started with Pysic, you'll need to have Python installed on your system. You can install the required dependencies using `pip`:

```sh
pip install requests tqdm
```

## Usage

Here's a quick example of how to use Pysic:

```python
from tidal import api
from tidal import downloader

# Search for songs
tracks = api.search_songs("hello", artist="adele")

# Get the URL for the first track
track = api.get_track_url(tracks[0], "LOSSLESS")

# Download the track
d = downloader.Downloader()
d.download_track(track.get_track_url(), "hello.mp3")
```

## Project Structure

- `main.py`: The main entry point of the application.
- `tidal/api.py`: Contains functions to interact with the Tidal API.
- `tidal/downloader.py`: Contains the `Downloader` class for downloading tracks.
- `tidal/models.py`: Defines the `Track` model.

## Contributing

As this is my first project, I'm open to any suggestions and contributions. Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.

---

## Acknowledgements

Special thanks to [sachinsenal0x64](https://github.com/sachinsenal0x64/hifi-tui/) for providing the Tidal API used in this project.

---

Thank you for checking out Pysic! Stay tuned for more updates as I continue to learn and improve my Python skills.
