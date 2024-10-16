from pathlib import Path
import os

class DocFolder:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def search_files(self, doc_names_list):
        try:
            # Verifica se o caminho fornecido é uma pasta válida
            if not self.folder_path.is_dir():
                raise FileNotFoundError
            
            # Normaliza os nomes na lista para evitar problemas com maiúsculas/minúsculas
            doc_names_list_lower = [name.lower() for name in doc_names_list]
            
            for file in os.listdir(self.folder_path):
                # Remove a extensão do arquivo e converte para minúsculas
                file_without_extension = os.path.splitext(file)[0].lower()

                # Verifica se o nome do arquivo sem extensão está na lista fornecida
                if file_without_extension in doc_names_list_lower :
                    print(f"O arquivo '{file}' está na pasta!.")

        except FileNotFoundError:
            print(f"Erro: A pasta '{self.folder_path}' não foi encontrada.")
            



