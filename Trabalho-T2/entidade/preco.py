

class Preco:
    def __init__(self, postagem, valor, confirmacao): #verificar atributos, getters and setters
        self.__postagem = postagem
        self.__valor = valor
        self.__confirmacao = confirmacao
    
    @property
    def postagem(self):
        return self.__postagem
    
    @postagem.setter
    def postagem(self, postagem):
        self.__postagem = postagem
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def confirmacao(self):
        return self.__confirmacao
    
    @confirmacao.setter
    def confirmacao(self, confirmacao):
        self.__confirmacao = confirmacao