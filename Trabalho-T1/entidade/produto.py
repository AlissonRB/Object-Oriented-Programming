from entidade.preco import Preco
from entidade.qualificador import Qualificador
from entidade.categoria import Categoria
from entidade.supermercado import Supermercado

class Produto:
    def __init__(self, nome: str, descricao: str, codigo: int, supermercado: Supermercado, categoria: Categoria, qualificadores,usuario): #verificar todos os atributos,getters e setters
        self.__nome = nome
        self.__descricao = descricao
        self.__codigo = codigo
        self.__supermercado = supermercado
        self.__categoria = categoria
        self.__qualificadores = qualificadores
        self.__lista_precos = []
        self.__confirmacoes = None #pega o preco que tem mais confirmaçoes
        self.__usuario = usuario
    
    def add_preco(self, informacoes_preco): #rever esse comando
        preco_existe = False
        valor = informacoes_preco["valor"]
        data = informacoes_preco["data"]
        confirmacao = informacoes_preco["confirmacao"]
        for preco in self.__lista_precos:
            if preco.valor == valor:
                preco.confirmacao += 1
                preco_existe = True
        if preco_existe == False:
            novo_preco = Preco(data, valor, confirmacao)
            self.__lista_precos.append(novo_preco)

        self.maior_confirmacao()
    
    def maior_confirmacao(self):
        self.__confirmacoes = self.__lista_precos[0]
        for preco in self.__lista_precos:
            if preco.confirmacao > self.__confirmacoes.confirmacao:
                self.__confirmacoes = preco
    
    @property
    def nome(self):
        return self.__nome
    
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
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codig(self, codigo):
        self.__codig = codigo
    
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
    def lista_precos(self):
        return self.__lista_precos
    
    @lista_precos.setter
    def precos(self, precos):
        self.__lista_precos = precos
    
    @property
    def qualificadores(self):
        return self.__qualificadores
    
    @qualificadores.setter
    def qualificadores(self, qualificadores):
        self.__qualificadores = qualificadores
    
    @property
    def confirmacoes(self):
        return self.__confirmacoes
    
    @confirmacoes.setter
    def confirmacoes(self, confirmacoes):
        self.__confirmacoes = confirmacoes
    
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

