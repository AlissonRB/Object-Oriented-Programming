from limite.telaAbstrata import TelaAbstrata


class TelaPreco(TelaAbstrata):

    def add_preco(self):
        while True:
            valor = input("Valor do Produto(duas cadas decimais): ")
            try:
                novo_valor = float(valor)

                return novo_valor
            except : 
                print("Valor incorreto: Digite um valor numérico valido")
    
    def telaopcoes(self):
        pass
    
    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        pass
