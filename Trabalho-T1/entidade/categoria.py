

class Categoria:
    def __init__(self, descricao: str, codigo: int) -> None:
        self.__descricao = descricao
        self.__codigo = codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo