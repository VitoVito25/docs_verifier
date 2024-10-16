from modelo.DocNamesFile import *
from modelo.DocFolder import *
from util.UserInterface import *

def main():
    interface = UserInterface                     ## Inicia o objeto de interface do usuario
    doc_names = DocNamesFile("docNamesFile.txt")  ## Inicia o objeto com o caminho do arquivo com os nomes
    doc_folder = DocFolder("pastaProcurar")       ## Inicia o objeto com o caminho da pasta dos arquivos
    
    doc_names.read_names()
    # Verifica se a lista de nomes está vazia
    if not doc_names.names_list:
        print("Lista de documentos para procura vazia...")
        exit()  # Encerra o programa

    doc_folder.search_files(doc_names.names_list)
    interface.print_final_report(doc_folder)

main()
