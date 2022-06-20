from entidade.qualificador import Qualificador
from limite.tela_produto import TelaProduto
from entidade.categoria import Categoria
from entidade.supermercado import Supermercado
from entidade.produto import Produto
from entidade.preco import Preco
from random import randint

class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__lista_produtos = []
    
    def cadastrar_produto(self):
        #self.__controlador_sistema.controlador_mercado.lista_de_supermercados() # lista os supermercados
        nome_descricao = self.__tela_produto.pega_dados() #pega nome e descrição do produto
        nome = nome_descricao["nome"]
        descricao = nome_descricao["descricao"]
        self.__controlador_sistema.controlador_categoria.listar_categoria() # lista as categorias
        categoria = self.__controlador_sistema.controlador_categoria.pega_codigo() # pega a categoria
        info_preco = self.__controlador_sistema.controlador_preco.incluir_novo_preco() #add preco
        qualificador = self.__controlador_sistema.controlador_qualificador.incluir_qualificador() # adicina uma lista de qualificadores
        codigo = self.gerar_codigo()
        self.instancia_produto(nome, descricao, supermercado, categoria, qualificador, info_preco)
        #rever as excessoes
            

    def instancia_produto(self,nome, descricao, codigo, supermercado, categoria, qualificadores, info_preco):
        if (nome is not None) and isinstance(nome, str):
            if (descricao is not None) and isinstance(descricao, str):
                if (codigo is not None) and isinstance(codigo, int):
                    if (categoria is not None) and isinstance(categoria, Categoria):
                        if (info_preco is not None) and isinstance(info_preco,dict):
                            for qualificador in qualificadores:
                                if (qualificador is not None) and isinstance(qualificador, Qualificador):
                                    novo_produto = Produto(nome, descricao, codigo, supermercado, categoria, qualificadores, info_preco)
                                    self.__lista_produtos.append(novo_produto)
                                
                                #rever as excessoes

        pass
    def pesquisar_preco(self):  #fazer pesquisa por qualificador tambem
        produtos = []
        busca_nome = self.__tela_produto.pega_nome_produto()
        qualificador = self.__controlador_sistema.controlador_qualificador.qualificador_na_busca()
        if qualificador is None:
            for produto in self.__lista_produtos:
                if produto.nome == busca_nome:
                    produtos.append(produto) #sfazer pesquisa com qualificadores tambem
        ordenar = self.__tela_produto.pega_codigo("Ordenar resultados: 1 - Preço \n 2- Confirmações 3 - Data de Postagem:", [1, 2, 3])
        #ordena a lista de produtos
        self.__tela_produto.mostra_resultados_busca(produtos)

    def lancar_preco(self):
        produto_existe = False
        #lista supermercados
        #pega o supermercado
        self.__controlador_sistema.controlador_categoria.listar_categoria()
        categoria = self.__controlador_sistema.controlador_categoria.pega_codigo() # pega a categoria
        nome = self.__tela_produto.pega_nome_produto()
        qualificadores = self.__controlador_sistema.controlador_qualificador.incluir_qualificador() # adicina uma lista de qualificadores
        for produto in self.__lista_produtos: # checa se o produto existe
            if produto.supermercado == supermercado:
                if produto.categoria == categoria:
                    if produto.nome == nome:  #comparar qualificadores
                        produto_existe = True
                        if produto_existe == True:
                            info_preco = self.__controlador_sistema.controlador_preco.incluir_novo_preco()
                            
                        else:
                            self.__tela_produto.mostra_msg("Produto não encontrado")
                        #compara o preço e entao confirma ou adiciona um novo
        

    #talvexz tenha que especializar tipo produto.supermercado.nome
    def excluir_produto(self):
        produtos_excluir = []
        codigos_validos = []
        #seleciona o supermercado, lista os supermercados
        nome = self.__tela_produto.pega_nome_produto()
        for produto in self.__lista_produtos:
            if produto.supermercado == supermercado:
                if produto.nome == nome:
                    produtos_excluir.append(produto)
                    codigos_validos.append(produto.codigo)
        if len(produtos_excluir) == 0:
            self.__tela_produto.mostra_msg("Nenhum produto encontrado")
        else:
            self.__tela_produto.mostra_resultados_busca(produtos_excluir)
            excluir = self.__tela_produto.pega_codigo("Selecione o código do produto a excluir", codigos_validos)

        #o nome do produto
        #lista os produtos com essa caracteristica e dai o seleciona de acordo com o codigo
        pass

    def registros_de_um_produto(self):
        pass
        #Registros (inclusão, exclusão, alteração e listagem) de preços de produtos 
        #seleciona o supermercado
        #seleciona o nome e lista os produtos com esse nome
        # dai seleciona o codigo do produto
        #e gera um relatorio dos preços dele

    def relatorio(self):
        #produtos por supermercado,
        #evolução dos preços de um produto por data, com valor mais caro e mais barato já registrado
        
        lista_opcoes = {1: self.produtos_por_supermercado, 2: self.evolucao_precos, 0: self.abre_tela}

        while True:
            opcao_escolhida = self.__tela_produto.relatorios()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
    def produtos_por_supermercado(self):
        produtos = []
        #lista os supermercados
        #seleciona um e pra cada produto que tiver aquele supermercado printa ele
        #supermercado = pega um supermercado
        for item in self.__lista_produtos:
            if item.supermercado.nome == supermercado:
                produtos.append(item)
        self.__tela_produto.mostra_resultados_busca(produtos)


    def evolucao_precos(self):
        #seleciona um supermercado
        #digita um nome e pega um codigo, e para aquele produto faz:
        pass

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

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_produto, 2: self.pesquisar_preco, 3: self.lancar_preco, 4: self.excluir_produto,
                        5: self.registros_de_um_produto, 6: self.relatorio, 0: self.retornar}

        while True:
            opcoes = self.__tela_produto.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcoes]
            funcao_escolhida()
