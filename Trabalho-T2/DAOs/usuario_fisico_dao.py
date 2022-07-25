from DAOs.dao import DAO
from entidade.usuarioJuridico import UsuarioJuridico


# cada entidade terá uma classe dessa, implementação bem simples.
class UsuarioFisicoDao(DAO):
    def __init__(self):
        super().__init__('usuario_juridico.pkl')

    def add(self, usuario: UsuarioJuridico):
        if usuario is not None:
            super().add(usuario.email, usuario)

    def update(self, usuario: UsuarioJuridico):
        if usuario is not None:
            super().update(usuario.email, usuario)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key: str):
        if isinstance(key, str):
            return super().remove(key)
