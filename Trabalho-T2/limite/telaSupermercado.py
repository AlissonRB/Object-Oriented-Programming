from limite.telaAbstrata import TelaAbstrata


class TelaSupermercado(TelaAbstrata):
    def __init__(self):
        super().__init__()

    def telaopcoes(self):
        print("------Tela Mercado------")
        print("1 - Cadastrar Mercado")
        print("2 - Alterar Mercado")
        print("3 - Excluir Mercado")
        print("4 - Listar Mercados")
        print("0 - Voltar")
        opcao = self.le_numero_inteiro("Escolha sua opcao: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_supermercado(self):
        print("-----Digite os Dados-----")
        nome = input("Nome do Mercado :")
        endereco = input("Endereco: ")
        return {"nome": nome, "endereco": endereco}

    def mostra_dados_supermercado(self):
        pass

    def mensagem_pro_usuario(self, mensagem: str):
        print(mensagem)

    def seleciona_mercado(self):
        nome = input("Nome do Mercado que deseja selecionar: ")
        return {"nome": nome}

    def dados_dono(self):
        cnpj = input("Cnpj do Mercado")
        return {"cnpj": cnpj}

    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor Incorreto, Digite um Valor Valido")
                if inteiros_validos:
                    print("Valores Validos: ", inteiros_validos)
