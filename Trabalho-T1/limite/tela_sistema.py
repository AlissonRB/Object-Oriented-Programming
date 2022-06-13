from limite.abstracttela import Tela

class TelaSistema(Tela):
    #fazer o tratamento das entradas
    def tela_opcoes(self):
        print("-------- O preço está certo ---------")
        print("Escolha a opcao")
        print("1 - Produtos")
        print("2 - Usuarios")
        print("3 - Supermercados")
        print("4 - Categoria")
        print("0 - Logout")
        opcao = int(input("Escolha a opcao:"))
        return opcao