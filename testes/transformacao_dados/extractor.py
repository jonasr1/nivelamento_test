import pandas as pd
from pathlib import Path
import pdfplumber


class PDFDataExtractor:
    DEFAULT_COLUMNS = [
        'PROCEDIMENTO', 'RN', 'VIGÊNCIA', 'Odontológico', 'Ambulatório', 
        'HCO', 'HSO', 'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPÍTULO'
    ]

    def __init__(self, pdf_path: str | Path) -> None:
        self.pdf_path = Path(pdf_path)

    def _extract_raw_tables(self) -> list[list[list[str]]]:
        '''Extrai tabelas brutas do PDF, retornando uma lista de listas.'''
        tables = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                if table := page.extract_table():
                    tables.append(table)
        return tables

    def _normalize_tables(self, tables: list[list[list[str]]]) -> pd.DataFrame:
        '''Normaliza as tabelas para manter um conjunto fixo de colunas.'''
        all_data = [row for table in tables for row in table[1:]]  # Ignora os cabeçalhos extraídos
        # Criar DataFrame e garantir que tenha todas as colunas fixas
        df = pd.DataFrame(all_data, columns=self.DEFAULT_COLUMNS[:len(all_data[0])])
        for col in self.DEFAULT_COLUMNS: # Adiciona colunas ausentes para manter o padrão
            if col not in df.columns:
                df[col] = ''
        # Reorganiza as colunas para manter a ordem fixa
        return df[self.DEFAULT_COLUMNS]

    def extract_table(self) -> pd.DataFrame:
        '''Executa a extração e normalização das tabelas.'''
        raw_tables = self._extract_raw_tables()
        return self._normalize_tables(raw_tables)
