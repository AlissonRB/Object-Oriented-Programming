from DAOs.dao import DAO
from entidade.supermercado import Supermercado


# cada entidade terá uma classe dessa, implementação bem simples.
class MercadoDAO(DAO):
    def __init__(self):
        super().__init__('supermercado.pkl')

    def add(self, supermercado: Supermercado):
        if supermercado is not None:
            super().add(supermercado.nome, supermercado)

    def update(self, supermercado: Supermercado):
        if supermercado is not None:
            super().update(supermercado.nome, supermercado)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key: str):
        if isinstance(key, str):
            return super().remove(key)
