from pathlib import Path
import os

class DocFolder:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def is_pdf(file_name):
        """
        Verifica se o arquivo possui a extensão .pdf.
        
        :param file_name: Nome do arquivo a ser verificado.
        :return: True se o arquivo for um PDF, False caso contrário.
        
        """
        # Verifica se a extensão do arquivo é .pdf, ignorando diferenças de maiúsculas e minúsculas
        return os.path.splitext(file_name)[1].lower() == '.pdf'



    def search_files(self, doc_names_list):
        try:
            # Verifica se o caminho fornecido é uma pasta válida
            if not self.folder_path.is_dir():
                raise FileNotFoundError
            
            for file in os.listdir(self.folder_path):
                # Remove a extensão do arquivo e converte para minúsculas
                file_without_extension = os.path.splitext(file)[0].lower()

                # Verifica se o nome do arquivo sem extensão está na lista fornecida
                if file_without_extension in doc_names_list:
                    print(f"O arquivo '{file}' está na pasta!.")

        except FileNotFoundError:
            print(f"Erro: A pasta '{self.folder_path}' não foi encontrada.")
            



