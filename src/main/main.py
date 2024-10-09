from modelo.DocNamesFile import *

def main():
    caminho_do_arquivo = "docNamesFile.txt"
    doc_names = DocNamesFile(caminho_do_arquivo)
    doc_names.read_save_names()
    doc_names.print_names()

main()
