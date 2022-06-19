from limite.tela_produto import TelaProduto
from random import randint

class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__lista_produtos = []
    
    def cadastrar_produto(self):

        nome_descricao = self.__tela_produto.pega_dados() #pega nome e descrição do produto
        self.__controlador_sistema.controlador_categoria.listar_categoria() # lista as categorias
        categoria = self.__controlador_sistema.controlador_categoria.pega_codigo() # pega o codigo da categoria
        preco = self.__controlador_sistema.controlador_preco.incluir_novo_preco() #add preco
        print(preco.valor, preco.postagem, preco.confirmacao)
        qualificador = self.__controlador_sistema.controlador_qualificador.incluir_qualificador() # adicina uma lista de qualificadores
        codigo = self.gerar_codigo()
        if codigo is not None:
            pass
            #instancia o produto

    def pesquisar_preco(self):  #fazer pesquisa por qualificador tambem
        produtos = []
        busca_nome = self.__tela_produto.pega_nome_produto()
        qualificador = self.__controlador_sistema.controlador_qualificador.qualificador_na_busca()
        if qualificador is None:  
            for produto in self.__lista_produtos:
                if produto.nome == busca_nome:
                    produtos.append(produto)
        ordenar = self.__tela_produto.pega_codigo("Ordenar resultados: 1 - Preço \n 2- Confirmações 3 - Data de Pestagem:", [1, 2, 3])
        #ordena a lista de produtos
        

    def lancar_preco(self):
        produto = False
        #lista supermercados
        #pega o supermercado
        self.__controlador_sistema.controlador_categoria.listar_categoria()
        categoria = self.__controlador_sistema.controlador_categoria.pega_codigo() # pega a categoria
        nome = self.__tela_produto.pega_nome_produto()
        qualificadores = self.__controlador_sistema.controlador_qualificador.incluir_qualificador() # adicina uma lista de qualificadores
        for produto in self.__lista_produtos: # checa se o produto existe
            if produto.supermercado == supermercado:
                if produto.categoria == categoria:
                    if produto.nome == nome:
                        produto = True
                        #comparar qualificadores
        if produto == True:
            pass
        #compara o preço e entao confirma ou adiciona um novo
        


    def excluir_produto(self):
        #seleciona o supermercado
        #seleciona a categoria
        #o nome do produto
        #lista os produtos com essa caracteristica e dai o seleciona de acordo com o codigo
        pass

    def buscar_produto(self):
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
        #lista os supermercados
        #seleciona um e pra cada produto que tiver aquele supermercado printa ele
        pass


    def evolucao_precos(self):
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
