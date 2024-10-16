from pathlib import Path
import os

class DocNamesFile:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.names_list = []

    def remove_extension(self):
        """
            Metodo para remover extensões da lista de nomes da classe
        """
        names_list_without_extension = []
        for name in self.names_list:
            name_without_extension = os.path.splitext(name)[0]
            names_list_without_extension.append(name_without_extension)
        self.names_list = names_list_without_extension

    def read_names(self):
        """
            Metodo para ler os nomes dos arquivos dentro de um arquivo txt
            :return True: Caso a leitura dos nomes do arquivo de certo
            :return None: Caso a leitura dos nomes de erro
        """
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                # Lê todas as linhas, removendo quebras de linha e espaços desnecessários
                names_list = [line.strip() for line in file.readlines()]
                self.names_list = names_list ## A lista de nomes encontrado é colocado dentro do atributo
                self.remove_extension()
                return True
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.file_path.name}' não encontrado no diretório {self.file_path.parent}.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return None
        
    