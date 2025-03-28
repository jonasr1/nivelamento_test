from .config import DEFAULT_DOWNLOAD_PATH
from .file_management.downloader import FileDownloader
from .file_management.saver import LocalFileSaver
from .file_management.zip_compressor import ZipCompressor
from .web_scraper import WebScraper

URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'


def main():
    'Executa o processo de Web Scraping para baixar PDFs da página especificada.'''
    print('Iniciando Web Scraper...')

    downloader = FileDownloader()
    file_saver = LocalFileSaver()

    scraper = WebScraper(URL, downloader, file_saver,)

    scraper.download_pdfs()
    
    compressor = ZipCompressor()
    compressor.compress(DEFAULT_DOWNLOAD_PATH, 'anexos')
    
    print('Processo concluído!')


if __name__ == '__main__':
    main()
