import requests
from tqdm import tqdm

class Downloader:
    def __init__(self):
        pass

    def download_track(self, track_url, file_path):
        response = requests.get(track_url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        with open(file_path, 'wb') as file, tqdm(
            desc=file_path,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                bar.update(len(data))

    def download_tracks(self, tracks):
        for track in tracks:
            self.download_track(track['url'], track['file_path'])

