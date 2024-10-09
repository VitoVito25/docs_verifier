from pathlib import Path

class DocNamesFile:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.names_list = []

    def read_save_names(self):
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                # Lê todas as linhas, removendo quebras de linha e espaços desnecessários
                self.names_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.file_path.name}' não encontrado no diretório {self.file_path.parent}.")
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")

    def print_names(self):
        for name in self.names_list:
            print(name)