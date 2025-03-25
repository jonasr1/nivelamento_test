import os
import traceback
from pathlib import Path
from urllib.parse import urlparse

from file_management.interfaces import Downloader, FileSaver
from file_management.pdf_link_extractor import PDFLinkExtractor
from file_management.progress_download import ProgressDownloader
from config import DEFAULT_DOWNLOAD_PATH

class WebScraper:
    def __init__(
        self,
        url: str,
        downloader: Downloader,
        file_saver: FileSaver,
        keywords: list[str] | None = None,
        download_path: str | None = None,
    ) -> None:
        """
        Inicializa o WebScraper.

        :param url: URL da página com os links dos PDFs.
        :param downloader: Objeto que sabe como baixar arquivos.
        :param file_saver: Objeto que sabe como salvar os arquivos no sistema.
        """
        self.extractor = PDFLinkExtractor(url, keywords)
        self.downloader = downloader
        self.file_saver = file_saver
        self.download_path = (Path(download_path) if download_path else DEFAULT_DOWNLOAD_PATH)

    def download_pdfs(self):
        """Baixa os PDFs encontrados na página e salva-os no diretório especificado."""
        self.download_path.mkdir(parents=True, exist_ok=True)
        if not (pdf_links := self.extractor.get_pdf_links()):
            print("Nenhum PDF encontrado para download")
            return
        downloader = ProgressDownloader(self.downloader)
        for link in pdf_links:
            file_name = os.path.basename(urlparse(link).path)
            file_path = os.path.join(self.download_path, file_name)
            try:
                content = downloader.download_file(link)
                self.file_saver.save(content, file_path)
                print(f"PDF {file_name} baixado com sucesso.\n")
            except Exception:
                print(f"Erro ao baixar {file_name}")
                traceback.print_exc()
