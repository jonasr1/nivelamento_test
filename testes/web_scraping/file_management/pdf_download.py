import traceback

from downloader import Downloader, FileDownloader
from saver import FileSaver


class PDFDownloader(FileDownloader):
    def __init__(self, downloader: Downloader, file_saver: FileSaver) -> None:
        self.downloader = downloader
        self.file_saver = file_saver

    def download(self, url: str, destination: str) -> None:
        try:
            content = self.downloader.download_file(url)
            self.file_saver.save(content, destination)
            print(f'Arquivo salvo em {destination}')
        except Exception:
            print('Ocorreu um erro inesperado ao tentar baixar o arquivo:')
            traceback.print_exc()
