from controle.controlador_produto import ControladorProduto
from controle.controlador_categoria import ControladorCategoria
from controle.controlador_preco import ControladorPreco
from controle.controlador_qualificador import ControladorQualificador
from limite.tela_sistema import TelaSistema

from limite.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_preco = ControladorPreco(self)
        self.__controlador_qualificador = ControladorQualificador(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_produto(self):
        return self.__controlador_produto

    @property
    def controlador_categoria(self):
        return self.__controlador_categoria
    
    @property
    def controlador_preco(self):
        return self.__controlador_preco

    @property
    def controlador_qualificador(self):
        return self.__controlador_qualificador

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
        self.__controlador_categoria.abre_tela()

    def logout(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.chama_produtos, 2: self.chama_usuario, 3: self.chama_supermercado,
                        4: self.chama_categoria, 0: self.logout}

        while True:
            opcoes = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcoes]
            funcao_escolhida()
