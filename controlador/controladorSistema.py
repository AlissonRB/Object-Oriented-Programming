from controlador.controladorUsuario import ControladorUsuario
from controlador.controladorMercado import ControladorMercado
from tela.telaSistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controladorUsuario = ControladorUsuario(self)
        self.__controladorMercado = ControladorMercado(self)
        self.__telaSistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def pesquisar_produto(self):
        pass

    def chama_produto(self):
        pass

    def chama_usuario(self):
        self.__controladorUsuario.abretela()

    def chama_supermercado(self):
        self.__controladorMercado.abretela()

    def chama_categoria(self):
        pass

    def cria_dono(self):
        return self.__controladorUsuario.verifica_usuario_juridico()

    def logout(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.chama_usuario, 2: self.chama_supermercado, 0: self.logout}

        while True:
            opcao_escolhida = self.__telaSistema.telaopcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
