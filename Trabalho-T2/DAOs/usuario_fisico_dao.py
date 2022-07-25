from DAOs.dao import DAO
from entidade.usuarioFisico import UsuarioFisico


# cada entidade terá uma classe dessa, implementação bem simples.
class UsuarioFisicoDao(DAO):
    def __init__(self):
        super().__init__('usuario_fisico.pkl')

    def add(self, usuario: UsuarioFisico):
        if (usuario is not None):
            super().add(usuario.email, usuario)

    def update(self, usuario: UsuarioFisico):
        if (usuario is not None):
            super().update(usuario.email, usuario)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key: str):
        if isinstance(key, str):
            return super().remove(key)
