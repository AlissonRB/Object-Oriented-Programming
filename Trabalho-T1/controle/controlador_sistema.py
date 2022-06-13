from controle.controlador_produto import ControladorProduto
from controle.controlador_categoria import ControladorCategoria
from limite.tela_sistema import TelaSistema

from limite.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_categoria = ControladorCategoria(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def pesquisa_produto(self):
        pass

    def chama_produtos(self):
        self.__controlador_produto.abre_tela()

    def chama_usuario(self):
        pass

    def chama_supermercado(self):
        pass

    def chama_categoria(self):
        pass

    def logout(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.chama_produtos, 2: self.chama_usuario, 3: self.chama_supermercado,
                        4: self.chama_categoria, 0: self.logout}

        while True:
            opcoes = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcoes]
            funcao_escolhida()
