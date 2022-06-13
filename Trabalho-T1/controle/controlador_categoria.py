from limite.tela_categoria import TelaCategoria

class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_categorias = []
        self.__tela_categoria = TelaCategoria()
    
    def cadastrar_categoria(self):
        produto = self.__tela_categoria.pega_dados()

    def alterar_categoria(self):
        pass

    def excluir_categoria(self):
        pass

    def listar_categoria(self):
        pass

    def retornar(self):
        pass

    def abre_tela(self):
        opcoes = {1: self.cadastrar_categoria, 2: self.excluir_categoria, 3: self.listar_categoria}

        while True:
            opcoes = self.__tela_categoria.tela_opcoes()
            funcao_escolhida = opcoes[opcoes]
            funcao_escolhida()


