from entidade.usuarioAbstrato import Usuario


class UsuarioFisico(Usuario):
    def __init__(self, nome: str, email: str, cpf: str):
        super().__init__(nome, email)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
