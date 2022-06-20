from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria
from random import randint

class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_categorias = []
        self.__tela_categoria = TelaCategoria()
        #categoria cadastrada apenas para teste
        nova = Categoria("frios", 123)
        self.__lista_categorias.append(nova)
    
    def cadastrar_categoria(self):
        existe = False
        dados_categoria = self.__tela_categoria.pega_dados()
        for i in self.__lista_categorias:
            if  dados_categoria == i.descricao:
                existe = True
        if existe == False:
            codigo = self.gerar_codigo()
            if codigo != None:
                nova_categoria = Categoria(dados_categoria, codigo)
                self.__lista_categorias.append(nova_categoria)
                self.__tela_categoria.mostra_msg("Categoria cadastrado com sucesso!")
            else:
                self.__tela_categoria.mostra_msg("O codigo já está cadastrado!") #refazer
        else:
            self.__tela_categoria.mostra_msg("Categoria já cadastrada!")

    def gerar_codigo(self):
        existe  = False
        while True:
            codigo = randint(0, 500)
            for produto in self.__lista_produtos:
                if codigo == produto.codigo:
                    existe = True
            break
        if existe ==  False:
            return codigo
        else:
            return None

    def listar_categoria(self):
        for categoria in self.__lista_categorias:
            self.__tela_categoria.lista_categoria({"categoria": categoria.descricao, "codigo": categoria.codigo})  #REVER SE É ASSIM MESMO
    
    def pega_categoria_por_codigo(self, codigo: int):  #acho que não estou usando essa função mais
        for categoria in self.__lista_categorias:
            if (categoria.codigo == codigo):
                return categoria
            return None

    def pega_codigo(self):
        opcoes = []
        for categoria in self.__lista_categorias:  #serase
            opcoes.append(categoria.codigo)
        codigo = self.__tela_categoria.pega_codigo("Digite o código da categoria",opcoes)
        for categoria in self.__lista_categorias:
            if codigo == categoria.codigo:
                return categoria

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.cadastrar_categoria, 2: self.alterar_categoria, 3: self.excluir_categoria, 
                    4: self.listar_categoria, 0: self.retornar}

        while True:
            opcao = self.__tela_categoria.tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()


