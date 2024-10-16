
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
## ---- ##
Relatório de Processamento:
- Total de Exceções: {totalExceptionFiles}
- Exceções por Arquivos Não Encontrados: {len(doc_folder.notFoundFiles)}
- Exceções por Arquivos Corrompidos ou Senha: {len(doc_folder.corruptedFiles)}
- Exceções por Arquivos Nao PDF: {len(doc_folder.notPdfFiles)}
## ---- ##
- Total de Arquivos Sem Problemas: {totalSuccessFiles}
- Total de Nomes Procurados: {len(doc_folder.totalFiles)}
"""
        
        print(report)
    
    def print_not_pdf_files(doc_folder):
        """
        Imprime a lista de arquivos que não são PDFs.
        """
        print("=== Arquivos que não são PDFs ===")
        for file in doc_folder.notPdfFiles:
            print(file)


    def print_corrupted_files(doc_folder):
        """
        Imprime a lista de arquivos corrompidos ou protegidos.
        """
        print("=== Arquivos Corrompidos ou Protegidos ===")
        for file in doc_folder.corruptedFiles:
            print(file)


    def print_not_found_files(doc_folder):
        """
        Imprime a lista de arquivos que não foram encontrados.
        """
        print("=== Arquivos Não Encontrados ===")
        for file in doc_folder.notFoundFiles:
            print(file)

    def print_if_not_empty(doc_folder, file_list, print_function):
        """
        Verifica se a lista possui conteúdo e, se sim, chama a função de impressão correspondente.

        :param doc_folder: Instância do DocFolder contendo as listas.
        :param file_list: A lista de arquivos que será verificada.
        :param print_function: Função que será chamada para imprimir os dados, caso a lista não esteja vazia.
        """
        if file_list:  # Verifica se a lista não está vazia
            print_function(doc_folder)

    def print_details(self, doc_folder):
        """
        Chama as funções de impressão para cada categoria, se a lista correspondente não estiver vazia.
        """
        self.print_if_not_empty(doc_folder, doc_folder.notPdfFiles, self.print_not_pdf_files(doc_folder))
        self.print_if_not_empty(doc_folder, doc_folder.corruptedFiles, self.print_corrupted_files(doc_folder))
        self.print_if_not_empty(doc_folder, doc_folder.notFoundFiles, self.print_not_found_files(doc_folder))
