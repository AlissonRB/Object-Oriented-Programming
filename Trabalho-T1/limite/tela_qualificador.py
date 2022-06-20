

class TelaQualificador():

    def le_num_inteiro(self, mensagem, inteiros_validos):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor numérico valido")
                if inteiros_validos:
                    print("Valores validos:", inteiros_validos)

    def pega_codigo(self, mensagem, codigos_validos):
        num_opcao = self.le_num_inteiro(mensagem, codigos_validos)
        return num_opcao

    def pega_dados(self):
        titulo = input('Titulo Qualificador: ')
        descricao = input('Descricao Qualificador: ')
        return {"titulo": titulo, "descricao": descricao}