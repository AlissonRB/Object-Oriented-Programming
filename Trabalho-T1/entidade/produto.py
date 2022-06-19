from entidade.preco import Preco
from entidade.qualificador import Qualificador
from entidade.categoria import Categoria

class Produto:
    def __init__(self, nome: str, descricao: str, codigo: int, supermercado: Supermercado, categoria: Categoria, info_qualificadores: str): #verificar todos os atributos,getters e setters
        self.__nome = nome
        self.__descricao = descricao
        self.__codigo = codigo
        self.__supermercado = supermercado
        self.__categoria = categoria
        self.__info_qualificadores = info_qualificadores # para instanciar o qualificador
        self.__preco = {}
    
    @property
    def nome(self):
        return self.__nome
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @property
    def supermercado(self):
        return self.__supermercado
    
    @supermercado.setter
    def supermercado(self, supermercado):
        self.__supermercado = supermercado
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco
