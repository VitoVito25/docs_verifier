
class UserInterface :

    def __init__(self):
        self.active_interface  ## Variavel apenas para indicar se a interface esta ativa

    def print_doc_names(names_list):
        """
            Metodo para imprimir uma lista de nomes na tela
            :param name_list: Lista de nomes a serem impressos na tela
        """

        for name in names_list:
            print(name)
    
    def print_final_report(doc_folder):
        """
        Imprime o relatório final com as informações de DocManager.
        """

        totalSuccessFiles = len(doc_folder.totalFiles) - len(doc_folder.notPdfFiles) - len(doc_folder.corruptedFiles) - len(doc_folder.notFoundFiles)
        totalExceptionFiles = len(doc_folder.notPdfFiles) + len(doc_folder.corruptedFiles) + len(doc_folder.notFoundFiles)

        report = f"""
Relatório de Processamento:
- Total de Exceções: {totalExceptionFiles}
- Exceções por Arquivos Não Encontrados: {len(doc_folder.notFoundFiles)}
- Exceções por Arquivos Corrompidos ou Senha: {len(doc_folder.corruptedFiles)}
- Exceções por Arquivos Nao Encontrados: {len(doc_folder.notFoundFiles)}
## ---- ##
- Total de Arquivos Sem Problemas: {totalSuccessFiles}
- Total de Arquivos Processados: {len(doc_folder.totalFiles)}
"""
        
        print(report)
