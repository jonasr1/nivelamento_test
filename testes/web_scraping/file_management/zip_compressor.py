
import os
from pathlib import Path
import zipfile


class ZipCompressor:
    def __init__(self, output_folder: str | Path = '') -> None:
        '''
        Inicializa o compressor com um diretório para salvar os arquivos ZIP.

        Args:
            output_folder (str | Path): Pasta onde os arquivos ZIP serão salvos.
        '''
        self.output_folder = Path(output_folder) if output_folder else Path(__file__).parent.parent / 'compressed_files'
        self.output_folder.mkdir(parents=True, exist_ok=True)  
    
    def compress(self, source_folder: Path| str, zip_name_without_ext: str, compression=zipfile.ZIP_DEFLATED) -> None:
        '''
        Compacta todos os arquivos dentro da pasta source_folder em um arquivo zip.

        Args:
            source_folder (str): Caminho da pasta a ser comprimida.
            zip_name (str): Nome do arquivo ZIP (sem a extensão ".zip").
        '''
        source_folder = Path(source_folder)
        zip_path = self.output_folder / f'{zip_name_without_ext}.zip'
        with zipfile.ZipFile(zip_path, 'w', compression) as zipf:
            for root, _, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, source_folder))
        print(f"Arquivos comprimidos em {zip_path}")
