import traceback
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class PDFLinkExtractor:
    def __init__(self, base_url: str, keywords: list[str] | None = None) -> None:
        self.base_url = base_url
        self.keywords = keywords or ['Anexo I', 'Anexo II']
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    def get_pdf_links(self) -> list[str]:
        '''Extrai os links dos PDFs da página especificada.

        Returns:
            Lista de URLs absolutas para arquivos PDF encontrados

        Raises:
            requests.exceptions.RequestException: Se houver erro na requisição HTTP
        '''
        try:
            response = requests.get(self.base_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return self.__extract_pdf_links(soup)
        except requests.exceptions.RequestException:
            print(f'Erro ao acessar a URL: {self.base_url}')
            traceback.print_exc()
            return []

    def __extract_pdf_links(self, soup: BeautifulSoup) -> list[str]:
        '''Extrai links de PDF do objeto BeautifulSoup.'''
        pdf_links = []
        for link in soup.find_all('a', href=True):
            if any(keyword.rstrip('.') == link.text.rstrip('.') for keyword in self.keywords):
                if value_href := link.get('href'):  # type: ignore
                    if isinstance(value_href, list):
                        value_href = value_href[0]
                    pdf_links.append(urljoin(self.base_url, value_href))  # type: ignore
        return pdf_links
