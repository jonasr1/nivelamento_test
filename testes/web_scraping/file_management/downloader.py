import requests

from .interfaces import Downloader


class FileDownloader(Downloader):
    def download_file(self, url: str) -> bytes:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
