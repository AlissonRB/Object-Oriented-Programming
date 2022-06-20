from limite.abstracttela import Tela


class TelaProduto():
    #fazer tratamento de excessoes
    def tela_opcoes(self):
        print("-------- Produtos ----------")
        print("Escolha a opcao")
        print("1 - incluir Produto")
        print("2 - Pesquisar Precos de Produtos")
        print("3 - Lançar Preço")
        print("4 - Excluir Produto")
        print("5 - Registros de um Produto ")
        print("6 - Relatórios")
        print("0 - Retornar")
        # alterar produto talvez
        opcao = int(input("Escolha a opcao:"))
        return opcao
    
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
    
    def pega_dados(self):
        print("----- Cadastrar Produto -----")
        nome = input("Nome do Produto: ")
        descricao = input("Descrição: ")
        return {"nome": nome, "descricao": descricao}
    
    def pega_nome_produto(self):
        nome = input("Nome do Produto: ")
        return nome

    def mostra_resultados_busca(self, lista_busca):
        for produto in lista_busca:
            print("Resultados da Busca")
            print ("Produto: ", produto.nome)
            print("Codigo: ", produto.codigo)
            print("Local: ", produto.supermercado.nome) #mesmo esquema
            print("Preço: ", produto.preço) #colocar preço mais alto
    
    
    def buscar_produto(self):
        print("----- Pesquisar Preço de um Produto -----")
        nome = input('Nome do produto: ')
        while True:
            qualificador = input('Qualificador (opcional): ')
            if qualificador != None:
                descricao = input('Descrição do qualificador: ')
            else:
                break
        return {"nome": nome} # retorn qualificadores
    
    def relatorios(self):
        print("-------- Relatórios ----------")
        print("Escolha a opcao")
        print("1 - Produtos por Supermercado")
        print("2 - Evolução dos Preços")
        print("0 - Voltar ")
        opcao = self.le_num_inteiro("Selecione uma opção", [1, 2 ,0])
        return opcao

    def pega_opcao(self):
        num_opcao = self.le_num_inteiro("Escolha a opção: ")
        return num_opcao
    
    
    def pega_codigo(self, mensagem, codigos_validos):
        num_opcao = self.le_num_inteiro(mensagem, codigos_validos)
        return num_opcao
    
    def mostra_msg(self, msg):
        print(msg)