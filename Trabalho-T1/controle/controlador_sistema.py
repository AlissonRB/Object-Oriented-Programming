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
        pass

    def pesquisa_produto(self):
        pass

    def chama_produtos(self):
        pass

    def chama_usuario(self):
        pass

    def chama_supermercado(self):
        pass

    def chama_categoria(self):
        pass

    def logout(self):
        pass

    def abre_tela(self):
        pass
