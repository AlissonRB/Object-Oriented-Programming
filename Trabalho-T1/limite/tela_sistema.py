

class TelaSistema:
    #fazer o tratamento das entradas
    def tela_opcoes(self):
        print("-------- O preço está certo ---------")
        print("Escolha a opcao")
        print("1 - Pesquisar produtos")
        print("2 - Produtos")
        print("3 - Usuarios")
        print("4 - Supermercados")
        print("5 - Categoria")
        print("0 - Logout")
        opcao = int(input("Escolha a opcao:"))
        return opcao