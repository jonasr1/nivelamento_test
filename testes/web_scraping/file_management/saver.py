from .interfaces import FileSaver


class LocalFileSaver(FileSaver):
    def save(self, content: bytes, destination: str) -> None:
        with open(destination, 'wb') as f:
            f.write(content)
