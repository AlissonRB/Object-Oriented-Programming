

class TelaPreco():

    def add_preco(self):
        while True:
            valor = input("Valor do Produto(duas cadas decimais): ")
            try:
                novo_valor = float(valor)

                return novo_valor
            except : #except ValueError:
                print("Valor incorreto: Digite um valor numérico valido")
