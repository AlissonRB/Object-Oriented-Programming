from limite.tela_preco import TelaPreco
from entidade.preco import Preco
import datetime

class ControladorPreco:
    def __init__(self, controlador_preco):
        self.__controlador_preco = controlador_preco
        self.__tela_preco = TelaPreco()
    
    def incluir_novo_preco(self):
        valor = self.__tela_preco.add_preco()
        data = datetime.date.today()
        confirmacao = 1
        return {"data": data, "valor": valor, "confirmacao": confirmacao}