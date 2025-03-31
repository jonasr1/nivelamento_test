from pathlib import Path
from tkinter import filedialog, messagebox

from .extractor import PDFDataExtractor
from web_scraping.file_management.zip_compressor import ZipCompressor

def check_existing_file(file: Path) -> bool:
    '''Verifica se o arquivo já existe e pergunta ao usuário se deseja sobrescrever.'''
    if file.exists():
        response = messagebox.askyesno(
            'Sobrescrever arquivo?',
            f'O arquivo {file} já existe. Deseja sobrescrevê-lo?'
        )
        return response
    return True

def select_pdf() -> str:
    pdf_path = filedialog.askopenfilename(title='Selecione o arquivo PDF')
    if not pdf_path:
        print('Operação cancelada pelo usuário.')
        return ''
    return pdf_path

def main():
    output_dir = Path('testes/transformacao_dados/csv')  # Diretório onde os arquivos CSV serão salvos
    output_dir_zip = Path('testes/transformacao_dados/compressed_files')
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    if not (pdf_path := select_pdf()):
        return
    output_csv = output_dir / 'dados_extraidos.csv'
    if not check_existing_file(output_csv):
        return
    print('Extraíndo dados do PDF...')
    extractor = PDFDataExtractor(pdf_path)
    df = extractor.extract_table()
    
    print('Salvando dados em CSV...')
    df.to_csv(output_csv, index=False, encoding='UTF-8')
    
    print('Compactando arquivo...')
    compressor = ZipCompressor(output_folder=output_dir_zip)
    compressor.compress(source_folder=output_dir, zip_name_without_ext='Teste_Jonas_Renan')

    print('Processo concluído!')
if __name__ == '__main__':
    main()
