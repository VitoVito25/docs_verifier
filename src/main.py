from modelo.DocNamesFile import *
from modelo.DocFolder import *
from util.UserInterface import *

def main():
    interface = UserInterface                     ## Inicia o objeto de interface do usuario
    doc_names = DocNamesFile("docNamesFile.txt")  ## Inicia o objeto com o caminho do arquivo com os nomes
    doc_folder = DocFolder("pastaProcurar")
    
    names_list = doc_names.read_names()
    interface.print_doc_names(names_list)
    doc_folder.search_files(names_list)



main()
