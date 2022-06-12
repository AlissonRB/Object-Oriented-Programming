from limite.tela_qualificador import TelaQualificador

class ControladorQualificador:
    def __init__(self, controlador_qualificador):
        self.__controlador_qualificador = controlador_qualificador
        self.__tela_preco = TelaQualificador()