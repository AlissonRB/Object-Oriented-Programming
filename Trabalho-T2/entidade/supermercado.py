from entidade.usuarioJuridico import UsuarioJuridico


class Supermercado:
    def __init__(self, nome: str, endereco: str, dono: UsuarioJuridico):
        self.__nome = nome
        self.__endereco = endereco
        self.__dono = dono

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def dono(self):
        return self.__dono

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @dono.setter
    def dono(self, dono):
        self.__dono = dono
