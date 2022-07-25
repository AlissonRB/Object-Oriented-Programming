

class Qualificador:
    def __init__(self, titulo, descricao):
        self.__titulo = titulo
        self.__descricao = descricao
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def descricao(self):
        return self.__descricao
    
    #verificar os setters