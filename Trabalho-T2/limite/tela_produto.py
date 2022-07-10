from limite.telaAbstrata import TelaAbstrata


class TelaProduto(TelaAbstrata):
    #fazer tratamento de excessoes
    def telaopcoes(self):
        print("-------- Produtos ----------")
        print("1 - incluir Produto")
        print("2 - Pesquisar Precos de Produtos")
        print("3 - Lançar Preço")
        print("4 - Excluir Produto")
        print("5 - Registros de um Produto ")
        print("6 - Relatórios")
        print("7 - Excluir Preço")
        print("0 - Retornar")
        num_opcao = self.le_numero_inteiro("Escolha a opção:", [1,2,3,4,5,6,7,0])
        return num_opcao

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
                    print("Valores validos: ", inteiros_validos)
    
    def pega_dados(self):
        print("----- Cadastrar Produto -----")
        nome = input("Nome do Produto: ")
        if (nome is not None) and isinstance (nome, str):
            descricao = input("Descrição: ")
            if (descricao is not None) and isinstance (descricao, str):
                preco = self.pega_preço()
                mercado = input("Supermercado: ")
                return {"nome_produto": nome, "descricao": descricao,"preco": preco, "mercado": mercado}
            else:
                self.mensagem_pro_usuario("Descrição do produto não aceita")
        else:
            self.mensagem_pro_usuario("Nome do produto não aceito")

    def pega_nome(self, msg):
        nome = input(msg)
        return nome
    
    def pega_preço(self):
        while True:
            try:
                preco = float(input("Preço: " )) #converter para duas casas
                if not isinstance(preco,float):
                    raise ValueError
                return preco
            except ValueError:
                print("Valor inválido !")

    def produtos_por_mercado(self, info):
        print("Produto: ",info["nome"])
        print("Preço: {:.2f}".format(info["preco"]))
        print("Categoria: ",info["categoria"])
        print("Codigo: ",info["codigo"])
        print("-----------------------------")
    
    def mostra_resultados_busca(self, info):
        print("Produto: ",info["nome"])
        print("Qualificador: ",info["qualificador"])
        print("Preço: {:.2f}".format(info["preco"]))
        print("Mercado: ",info["mercado"])
        print("-----------------------------")

    def evolucao_precos(self,info):
        pass

    def mostra_registros(self, dados_registro):
        print(dados_registro["data"], dados_registro["operacao"], dados_registro["valor"])
        print("\n")

    def relatorios(self):
        print("-------- Relatórios ----------")
        print("Escolha a opcao")
        print("1 - Produtos por Supermercado")
        print("2 - Evolução dos Preços")
        print("3 - Lista de Preços de um Produto")
        print("0 - Voltar ")
        opcao = self.le_numero_inteiro("Selecione uma opção", [1, 2 , 3, 0])
        return opcao

    def pega_inteiro(self, msg):
        while True:
            try:
                codigo = int(input(msg))
                if not isinstance(codigo,int):
                    raise ValueError
                return codigo
            except ValueError:
                print("Valor inválido:")
    
    def pega_float(self, msg):
        while True:
            try:
                codigo = float(input(msg))
                if not isinstance(codigo,float):
                    raise ValueError
                return codigo
            except ValueError:
                print("Valor inválido:")

    def mensagem_pro_usuario(self, msg):
        print(msg)
        print("\n")
