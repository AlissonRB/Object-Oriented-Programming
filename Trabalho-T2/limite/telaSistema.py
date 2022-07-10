from limite.telaAbstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    def __init__(self):
        super().__init__()

    def le_numero_inteiro(self, mensagem, inteiros_validos):
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

    def telaopcoes(self):
        print("------Escolha De Telas------")
        print("Escolha a opcao")
        print("1 - Produtos")
        print("2 - Usuarios")
        print("3 - Supermercados")
        print("4 - Categoria")
        print("0 - Voltar Para Tela Inicial")
        opcao = self.le_numero_inteiro('Escolha sua opcao: ', [1, 2,3,4,0])
        return opcao
