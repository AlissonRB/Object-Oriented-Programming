from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria
from random import randint

class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_categorias = []
        self.__tela_categoria = TelaCategoria()
    
    def cadastrar_categoria(self):
        existe = False
        dados_categoria = self.__tela_categoria.pega_dados()
        for i in self.__lista_categorias:
            if  dados_categoria == i.descricao:
                existe = True
        if existe == False:
            codigo = self.gerar_codigo()
            nova_categoria = Categoria(dados_categoria, codigo)
            self.__lista_categorias.append(nova_categoria)
            self.__tela_categoria.mostra_msg("Categoria cadastrado com sucesso!")
        else:
            self.__tela_categoria.mostra_msg("Categoria já cadastrada!")

    def alterar_categoria(self):
        pass

    def gerar_codigo(self):
        existe  = False
        codigo = randint(0, 100)
        while True:
            codigo = randint(0, 100)
            for categoria in self.__lista_categorias:
                if codigo == categoria.codigo:
                    existe = True
            if existe ==  False:
                break
        return codigo

    def excluir_categoria(self): 
        pass

    def listar_categoria(self):
        for categoria in self.__lista_categorias:
            self.__tela_categoria.lista_categoria({"categoria": categoria.descricao, "codigo": categoria.codigo})  #REVER SE É ASSIM MESMO
    
    def pega_categoria_por_codigo(self, codigo: int):
        for categoria in self.__lista_categorias:
            if (categoria.codigo == codigo):
                return categoria
            return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.cadastrar_categoria, 2: self.alterar_categoria, 3: self.excluir_categoria, 
                    4: self.listar_categoria, 0: self.retornar}

        while True:
            opcao = self.__tela_categoria.tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()


