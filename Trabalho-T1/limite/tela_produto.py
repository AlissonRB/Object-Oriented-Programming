from limite.abstracttela import Tela


class TelaProduto():
    #fazer tratamento de excessoes
    def tela_opcoes(self):
        print("-------- Produtos ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Produto")
        print("2 - Buscar Produto")
        print("3 - Excluir Produto")
        print("5 - Registros de um Produto ")
        print("4 - Relatórios")
        print("0 - Retornar")
        # alterar produto talvez
        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    def pega_dados(self):
        print("----- Cadastrar Produto -----")
        nome = input("Nome do Produto: ")
        descricao = input("Descrição: ")
        supermercado = input ("Supermercado: ")
        categoria = input("categoria: ")
        titulo_qualificador = input("Título Qualificador: ")  
        descricao_qualificador = input("Descrição Qualifcador: ")
        return {"nome": nome, "descricao": descricao, "supermercado": supermercado, 
                "categoria": categoria, "titulo_qualificador": titulo_qualificador, 
                "descricao_qualificador": descricao_qualificador }
        
        # o produto pode receber mais de um qualificador
        #categoria e supermercado tem que estar cadastrados