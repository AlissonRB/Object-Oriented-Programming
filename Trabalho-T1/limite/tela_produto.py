from limite.telaAbstrata import TelaAbstrata


class TelaProduto(TelaAbstrata):
    #fazer tratamento de excessoes
    def tela_opcoes(self):
        print("-------- Produtos ----------")
        print("1 - incluir Produto")
        print("2 - Pesquisar Precos de Produtos")
        print("3 - Lançar Preço")
        print("4 - Excluir Produto")
        print("5 - Registros de um Produto ")
        print("6 - Relatórios")
        print("0 - Retornar")
        # alterar produto talvez
        num_opcao = self.le_numero_inteiro("Escolha a opção:", [1,2,3,4,5,6,0])
        return num_opcao

    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        pass
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
        descricao = input("Descrição: ")
        mercado = input("Supermercado: ")
        usuario = input("Email do Usuario: ")
        tipo_usuario = self.le_numero_inteiro("1 - Usuário Fisico \n2 - Usuário Jurídico", [1,2])
        return {"nome_produto": nome, "descricao_produto": descricao, "mercado": mercado, "usuario": usuario,"tipo_usuario": tipo_usuario}

    def pega_nome(self, msg):
        nome = input(msg)
        return nome

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
        print(info[""])
        print(info[""])
        print(info[""])

    def relatorios(self):
        print("-------- Relatórios ----------")
        print("Escolha a opcao")
        print("1 - Produtos por Supermercado")
        print("2 - Evolução dos Preços")
        print("0 - Voltar ")
        opcao = self.le_numero_inteiro("Selecione uma opção", [1, 2 ,0])
        return opcao
    
    def telaopcoes(self):
        pass

    def pega_opcao(self):
        num_opcao = self.le_numero_inteiro("Escolha a opção: ")
        return num_opcao

    def pega_codigo(self, mensagem, codigos_validos):
        num_opcao = self.le_numero_inteiro(mensagem, codigos_validos)
        return num_opcao

    def mensagem_pro_usuario(self, msg):
        print(msg)
