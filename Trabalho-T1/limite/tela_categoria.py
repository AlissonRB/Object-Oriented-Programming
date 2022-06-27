from limite.telaAbstrata import TelaAbstrata

class TelaCategoria(TelaAbstrata):
    pass

    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
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

    def telaopcoes(self):
        print("-------- Categoria ----------")
        print("1 - Incluir Categoria")
        print("2 - Alterar Categorias ")
        print("3 - Excluir Categorias ")
        print("4 - Listar Categorias ")
        print("0 - Retornar")
        num_opcao = self.le_numero_inteiro("Escolha a opção: ",[1,2,3,4,0])
        return num_opcao

    def pega_dados(self):
        print("---- Cadastrar Categoria ----")
        categoria = input("Nome da Categoria: ")
        return categoria
    
    def pega_codigo(self, mensagem, codigos_validos):
        num_opcao = self.le_numero_inteiro(mensagem, codigos_validos)
        return num_opcao
    
    def lista_categoria(self, info_categoria):
        print("CATEGORIA:", info_categoria["categoria"], "CODIGO:", info_categoria["codigo"] )
    
    def mostra_msg(self, msg):
        print(msg)
