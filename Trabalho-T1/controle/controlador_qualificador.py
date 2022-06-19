from limite.tela_qualificador import TelaQualificador
from entidade.qualificador import Qualificador

class ControladorQualificador:
    def __init__(self, controlador_qualificador):
        self.__controlador_qualificador = controlador_qualificador
        self.__tela_qualificador = TelaQualificador()

    def novo_qualificador(self):
        info_qualificador = self.__tela_qualificador.pega_dados()
        titulo =  info_qualificador["titulo"]
        descricao =  info_qualificador["descricao"]
        qualificador = Qualificador(titulo, descricao)
        return qualificador
    
    def inclui_qualificador(self):
        qualificadores = []
        while True:
            novo_qualificador = self.novo_qualificador()
            qualificadores.append(novo_qualificador)
            continuar = self.__tela_qualificador.pega_codigo("Adicionar mais Qualificadores ?\n 1 - Sim\n 2 - Não",[1,2])
            if continuar == 2:
                break
        return qualificadores
    
    def qualificador_na_busca(self):
        add_qualificador = self.__tela_qualificador.pega_codigo("Adicionar Qualificador ?\n 1 - Sim\n 2 - Não",[1,2])
        if add_qualificador == 1:
            qualificador = self.inclui_qualificador()
            return qualificador
        