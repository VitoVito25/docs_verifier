from pathlib import Path
import PyPDF2
import os

class DocFolder:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        self.totalFiles = []
        self.notPdfFiles = []
        self.corruptedFiles = []
        self.notFoundFiles = []

    def is_pdf(self, file_name):
        """
        Verifica se o arquivo possui a extensão .pdf.
        
        :param file_name: Nome do arquivo a ser verificado.
        :return: True se o arquivo for um PDF, False caso contrário.

        """
        # Verifica se a extensão do arquivo é .pdf, ignorando diferenças de maiúsculas e minúsculas
        return os.path.splitext(file_name)[1].lower() == '.pdf'


    def test_pdf_open(self, file_name):
        """
        Tenta abrir um arquivo PDF e verifica se ele está corrompido ou protegido.
        
        :param file_name: Nome do arquivo PDF (sem o caminho completo).
        :return: True se o PDF pode ser aberto, False caso contrário.
        """

        # Constrói o caminho completo do arquivo PDF
        file_path = self.folder_path / file_name
        
        try:
            with open(file_path, 'rb') as file:
                # Tenta ler o PDF usando PyPDF2
                reader = PyPDF2.PdfReader(file)
                
                # Tenta acessar as páginas do PDF
                if reader.pages:
                    return True
        except (PyPDF2.errors.PdfReadError):
            # Caso o PDF esteja corrompido
            return False

    def search_files(self, doc_names_list):
        """
        Função para procurar arquivos com base em uma lista dentro da pasta
        
        :param doc_names_list: Lista de nomes a serem procurados
        """

        doc_status = {name : False for name in doc_names_list}
        self.totalFiles = doc_names_list

        try:
            # Verifica se o caminho fornecido é uma pasta válida
            if not self.folder_path.is_dir():
                raise FileNotFoundError
            
            for file in os.listdir(self.folder_path):

                # Remove a extensão do arquivo e converte para minúsculas
                file_without_extension = os.path.splitext(file)[0].lower()

                # Verifica se o nome do arquivo sem extensão está na lista fornecida
                if file_without_extension in doc_names_list:
                    doc_status[file_without_extension] = True # Atualiza o status para encontrado

                    ## Verifica se é um PDF
                    if not self.is_pdf(file):
                        self.notPdfFiles.append(file)
                        continue

                    ## Verifica se esta corrompido
                    if not self.test_pdf_open(file):
                        self.corruptedFiles.append(file)
                        continue
                
            self.notFoundFiles = [name for name, found in doc_status.items() if not found]
                    
        except FileNotFoundError:
            print(f"Erro: A pasta '{self.folder_path}' não foi encontrada.")

    

            



