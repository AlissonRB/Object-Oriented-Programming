from limite.tela_qualificador import TelaQualificador
from entidade.qualificador import Qualificador

class ControladorQualificador:
    def __init__(self, controlador_qualificador):
        self.__controlador_qualificador = controlador_qualificador
        self.__tela_qualificador = TelaQualificador()

    def incluir_qualificador(self):
        info_qualificador = self.__tela_qualificador.pega_dados()
        titulo =  info_qualificador["titulo"]
        descricao =  info_qualificador["descricao"]
        qualificador = Qualificador(titulo, descricao)
        return qualificador