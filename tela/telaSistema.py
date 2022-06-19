from tela.telaAbstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    def __init__(self):
        super().__init__()

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

    def telaopcoes(self):
        print("------Escolha De Telas------")
        print("1 - Opcoes Usuarios")
        print("2 - Opcoes Mercado")
        print("0 - Encerrar Sistema")
        opcao = self.le_numero_inteiro('Escolha sua opcao: ', [1, 2, 0])
        return opcao
