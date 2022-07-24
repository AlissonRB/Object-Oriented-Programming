from DAOs.dao import DAO
from entidade.categoria import Categoria

#cada entidade terá uma classe dessa, implementação bem simples.
class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categoria.pkl')

    def add(self, categoria: Categoria):
        if((categoria is not None) and isinstance(categoria, Categoria) and isinstance(categoria.nome, str)):
            super().add(categoria.nome, categoria)

    def update(self, categoria: Categoria):
        if((categoria is not None) and isinstance(categoria, Categoria) and isinstance(categoria.nome, str)):
            super().update(categoria.nome, categoria)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)
        else:
            return None

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)