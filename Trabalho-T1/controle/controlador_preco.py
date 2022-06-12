from limite.tela_preco import TelaPreco

class ControladorPreco:
    def __init__(self, controlador_preco):
        self.__controlador_preco = controlador_preco
        self.__tela_preco = TelaPreco()