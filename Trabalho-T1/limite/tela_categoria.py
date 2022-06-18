from limite.abstracttela import Tela

class TelaCategoria(Tela):
    pass

    def tela_opcoes(self):
        print("-------- Categoria ----------")
        print("Escolha a opcao")
        print("1 - Incluir Categoria")
        print("2 - Alterar Categoria")
        print("3 - Excluir Categoria") #rever esse comando
        print("4 - Listar Categorias ")
        print("0 - Retornar")
        # alterar categoria talvez
        opcao = int(input("Escolha a opcao:"))
        return opcao

    def pega_dados(self):
        print("---- Cadastrar Categoria ----")
        categoria = input("Nome da Categoria: ")
        return categoria
    
    def lista_categoria(self, info_categoria):
        print("CATEGORIA:", info_categoria["categoria"], "CODIGO:", info_categoria["codigo"] )
    
    def mostra_msg(self, msg):
        print(msg)