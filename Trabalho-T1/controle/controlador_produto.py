from limite.tela_produto import TelaProduto

class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__lista_produtos = []
    
    def cadastrar_produto(self):

        #nome_descricao = self.__tela_produto.pega_dados()
        #self.__controlador_sistema.controlador_categoria.listar_categoria()
        #swhile True:
            #codigo_categoria = self.__tela_produto.pega_opcao()
            #if codigo_categoria == 0: # isso é para sair da operação , ainda não está implenteada
                #break
            #categoria = self.__controlador_sistema.controlador_categoria.pega_categoria_por_codigo(codigo_categoria)
            #if categoria is not None:
                #break
            #else:
                #self.__tela_produto.mostra_msg('Codigo da categoria não encontrado')
        #preco = self.__controlador_sistema.controlador_preco.incluir_novo_preco()
        #print(preco.valor, preco.postagem, preco.confirmacao)
        qualificador = self.inclui_qualificador()

        
    def inclui_qualificador(self):
        qualificadores = []
        while True:
            add_qualificador = self.__controlador_sistema.controlador_qualificador.incluir_qualificador()
            qualificadores.append(add_qualificador)
            self.__tela_produto.mostra_msg('Adicionar mais qualificadores ?')
            self.__tela_produto.mostra_msg('0 - SIM')
            self.__tela_produto.mostra_msg('1 - NÂO')
            opcao = self.__tela_produto.pega_opcao()
            if opcao == 1:
                break
        return qualificadores

    def pesquisar_produto(self):
        pass

    def lancar_preco(self):
        pass

    def excluir_produto(self):
        pass

    def buscar_produto(self):
        pass

    def registros_de_um_produto(self):
        pass

    def relatorio(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_produto, 2: self.pesquisar_produto, 3: self.lancar_preco, 4: self.excluir_produto,
                        5: self.registros_de_um_produto, 6: self.relatorio, 0: self.retornar}

        while True:
            opcoes = self.__tela_produto.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcoes]
            funcao_escolhida()
