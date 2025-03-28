import requests
from tqdm import tqdm

import os
from urllib.parse import urlparse

from .interfaces import Downloader


class ProgressDownloader:
    def __init__(self, downloader: Downloader) -> None:
        self.downloader = downloader

    def download_file(self, url: str) -> bytes:
        '''
        Baixa um arquivo com exibição de progresso.
        '''
        response = requests.get(url, stream=True)
        response.raise_for_status()
        file_name = os.path.basename(urlparse(url).path)
        total_size = int(response.headers.get('content-length', 0))
        content = bytearray()
        with tqdm(
            total=total_size,
            unit='B',
            unit_scale=True,
            desc=f'Baixando: {file_name}',
            ncols=80,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    content.extend(chunk)
                    pbar.update(len(chunk))
        return bytes(content)
