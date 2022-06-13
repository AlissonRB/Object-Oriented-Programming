from limite.abstracttela import Tela

class TelaCategoria(Tela):
    pass

    def tela_opcoes():
        print("-------- Categoria ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Categoria")
        print("2 - Excluir Categoria") #rever esse comando
        print("3 - Listar Categorias ")
        print("0 - Retornar")
        # alterar categoria talvez
        opcao = int(input("Escolha a opcao:"))
        return opcao

    def pega_dados(self):
        pass