from abc import ABC, abstractmethod


class TelaAbstrata(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def telaopcoes(self):
        pass

    @abstractmethod
    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        pass

