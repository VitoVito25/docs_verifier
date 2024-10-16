from pathlib import Path

class DocNamesFile:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def read_names(self):
        """
            Metodo para ler os nomes dos arquivos dentro de um arquivo txt
            :param name_list: Lista de nomes a serem impressos na tela
        """
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                # Lê todas as linhas, removendo quebras de linha e espaços desnecessários
                names_list = [line.strip() for line in file.readlines()]
                return names_list ## Retorna um array com os nomes dos arquivos
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.file_path.name}' não encontrado no diretório {self.file_path.parent}.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return None