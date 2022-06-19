from entidade.usuarioAbstrato import Usuario


class UsuarioJuridico(Usuario):
    def __init__(self, nome: str, email: str, cnpj: str):
        super().__init__(nome, email)
        self.__cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
