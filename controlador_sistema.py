from controle.controlador_produto import ControladorProduto
from controle.controlador_categoria import ControladorCategoria
from controle.controlador_preco import ControladorPreco
from controle.controlador_qualificador import ControladorQualificador
from controle.controladorMercado import ControladorMercado
from controle.controladorUsuario import ControladorUsuario
from entidade.usuarioFisico import UsuarioFisico
from limite.telaSistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__usuario_logado = None  # associar o usuario que fez o login com esse atributo
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_preco = ControladorPreco(self)
        self.__controlador_qualificador = ControladorQualificador(self)
        self.__controladorMercado = ControladorMercado(self)
        self.__controladorUsuario = ControladorUsuario(self)
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

    @property
    def controladorMercado(self):
        return self.__controladorMercado

    @property
    def controladorUsuario(self):
        return self.__controladorUsuario

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, usuario_logado):
        self.__usuario_logado = usuario_logado

    def inicializa_sistema(self):
        self.controladorUsuario.abretela_inicial()

    def pesquisa_produto(self):
        pass

    def chama_produtos(self):
        self.__controlador_produto.abre_tela()

    def chama_usuario(self):
        self.__controladorUsuario.abretela()

    def chama_supermercado(self):
        self.__controladorMercado.abretela()

    def chama_categoria(self):
        self.__controlador_categoria.abre_tela()

    def cria_dono(self):
        return self.__controladorUsuario.verifica_usuario_juridico()

    def voltar(self):
        self.__controladorUsuario.abretela_inicial()

    def abre_tela(self):
        lista_opcoes = {1: self.chama_produtos, 2: self.chama_usuario, 3: self.chama_supermercado,
                        4: self.chama_categoria, 0: self.voltar, }

        while True:
            opcoes = self.__tela_sistema.telaopcoes()
            funcao_escolhida = lista_opcoes[opcoes]
            funcao_escolhida()
