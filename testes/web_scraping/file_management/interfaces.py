from abc import ABC, abstractmethod


class Downloader(ABC):
    @abstractmethod
    def download_file(self, url: str) -> bytes:
        pass


class FileSaver(ABC):
    @abstractmethod
    def save(self, content: bytes, destination: str) -> None:
        pass
