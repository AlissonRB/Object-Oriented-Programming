from limite.abstracttela import Tela


class TelaProduto():
    #fazer tratamento de excessoes
    def tela_opcoes(self):
        print("-------- Produtos ----------")
        print("Escolha a opcao")
        print("1 - incluir Produto")
        print("2 - Pesquisar Produtos")
        print("3 - Lançar Preço")
        print("4 - Excluir Produto")
        print("5 - Registros de um Produto ")
        print("6 - Relatórios")
        print("0 - Retornar")
        # alterar produto talvez
        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    def pega_dados(self):
        print("----- Cadastrar Produto -----")
        nome = input("Nome do Produto: ")
        descricao = input("Descrição: ")
        return {"nome": nome, "descricao": descricao}
        
        # o produto pode receber mais de um qualificador
        #categoria e supermercado tem que estar cadastrados
    def pega_opcao(self):
        num_opcao = int(input("Escolha a opcao: "))
        return num_opcao
    
    def mostra_msg(self, msg):
        print(msg)