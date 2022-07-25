from abc import ABC, abstractmethod


class TelaAbstrata(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def telaopcoes(self):
        pass

 #    @abstractmethod
 #    def open(self):
 #        pass
 #
 #    @abstractmethod
 #    def close(self):
 #        pass
 #
 #    @abstractmethod
 #    def mensagem_pro_usuario(self, mensagem: str):
 #        pass
