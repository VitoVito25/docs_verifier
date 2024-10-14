from modelo.DocNamesFile import *
from util.UserInterface import *

def main():
    interface = UserInterface                     ## Inicia o objeto de interface do usuario
    doc_names = DocNamesFile("docNamesFile.txt")  ## Inicia o objeto com o caminho do arquivo com os nomes
    
    names_list = doc_names.read_names()

    interface.print_doc_names(names_list)



main()
