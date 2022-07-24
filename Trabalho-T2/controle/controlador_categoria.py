from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria
from DAOs.categoria_dao import CategoriaDAO
from random import randint

class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__categoria_DAO = CategoriaDAO()
        self.__tela_categoria = TelaCategoria()
    
    def cadastrar_categoria(self): #arrumar o cadastrar categoria para não cadastrar categorias duplicadas
        dados_categoria = self.__tela_categoria.pega_dados()
        if dados_categoria is not None:
            if (dados_categoria["nome"] is not None) and (dados_categoria["descricao"] is not None):
                verificar = self.__categoria_DAO.get(dados_categoria['nome'])
                if  verificar is None:
                    nova_categoria = Categoria(dados_categoria['nome'], dados_categoria['descricao'])
                    self.__categoria_DAO.add(nova_categoria)
                    self.__tela_categoria.mostra_msg("Categoria cadastrado com sucesso!")
                else:
                        self.__tela_categoria.mostra_msg("Categoria já está cadastrada")

    def gerar_codigo(self):
        existe  = False
        while True:
            codigo = randint(0, 500)
            for produto in self.__lista_categorias:
                if codigo == produto.codigo:
                    existe = True
            break
        if existe ==  False:
            return codigo
        else:
            return None

    def listar_categoria(self):
        dados = []
        for categoria in self.__categoria_DAO.get_all():
            dados.append({"nome": categoria.nome, "descricao": categoria.descricao})
        self.__tela_categoria.lista_categoria(dados)
    
    def pega_categoria_por_descricao(self, key):
        categoria = self.__categoria_DAO.get(key)
        if (categoria is not None) and isinstance(categoria, Categoria):
            return categoria
        return None
    
    def retorna_nomes_categorias(self):
        descricao = []
        for categoria in self.__categoria_DAO.get_all():
            descricao.append(categoria.nome)
        return descricao

    def pega_codigo(self):
        opcoes = []
        for categoria in self.__lista_categorias:
            opcoes.append(categoria.codigo)
        codigo = self.__tela_categoria.pega_codigo("Digite o código da categoria",opcoes)
        for categoria in self.__lista_categorias:
            if codigo == categoria.codigo:
                return categoria

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def alterar_categoria(self):
        nome_categoria = self.__tela_categoria.pega_nome()
        if nome_categoria is not None:
            categoria = self.pega_categoria_por_descricao(nome_categoria)
            if (categoria is not None):
                nova_descricao = self.__tela_categoria.pega_descricao()
                categoria.descricao = nova_descricao
                self.__categoria_DAO.update(categoria)
                self.__tela_categoria.mostra_msg("Categoria alterada")
            
            else:
                self.__tela_categoria.mostra_msg("Categoria não encontrada")

    def excluir_categoria(self):
        nome_categoria = self.__tela_categoria.pega_nome()
        if nome_categoria is not None:
            categoria = self.pega_categoria_por_descricao(nome_categoria)
            if (categoria is not None):
                self.__categoria_DAO.remove(categoria.nome)
                self.__tela_categoria.mostra_msg("Categoria excluida com sucesso")
            else:
                self.__tela_categoria.mostra_msg("Categoria não encontrada")

    def abre_tela(self):
        opcoes = {1: self.cadastrar_categoria, 2: self.alterar_categoria, 3: self.excluir_categoria, 
                    4: self.listar_categoria, 0: self.retornar}

        while True:
            opcao = self.__tela_categoria.telaopcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()
