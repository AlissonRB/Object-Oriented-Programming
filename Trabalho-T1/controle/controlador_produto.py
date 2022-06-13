from limite.tela_produto import TelaProduto

class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__lista_produtos = []
    
    def cadastrar_produto(self):
        produto = self.__tela_produto.pega_dados()

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
        lista_opcoes = {1: self.cadastrar_produto, 2: self.buscar_produto, 3: self.excluir_produto,
                        4: self.registros_de_um_produto, 5: self.relatorio, 0: self.retornar}

        while True:
            opcoes = self.__tela_produto.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcoes]
            funcao_escolhida()
