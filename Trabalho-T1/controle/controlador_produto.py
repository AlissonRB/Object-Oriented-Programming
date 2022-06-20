from re import T
from entidade.qualificador import Qualificador
from limite.tela_produto import TelaProduto
from entidade.categoria import Categoria
from entidade.supermercado import Supermercado
from entidade.produto import Produto
from entidade.preco import Preco
from random import randint
from entidade.usuarioFisico import UsuarioFisico
from entidade.usuarioJuridico import UsuarioJuridico

class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__lista_produtos = []

    @property
    def usuario(self):
        return self.__usuario
    
    def cadastrar_produto(self):

        pega_dados = self.__tela_produto.pega_dados() #pega nome,descrição e mercado  do produto
        nome_mercado = pega_dados["mercado"]
        nome_produto = pega_dados["nome_produto"]
        descricao_produto = pega_dados["descricao_produto"]
        usuario = pega_dados["usuario"]
        tipo_usuario = pega_dados["tipo_usuario"]
        if tipo_usuario == 1:
            usuario_logado = self.__controlador_sistema.controladorUsuario.retorna_usuario_fisico(usuario)
        if tipo_usuario == 2:
            usuario_logado = self.__controlador_sistema.controladorUsuario.retorna_usuario_juridico(usuario)
        if (usuario_logado is not None):
            supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(nome_mercado)
            if (supermercado is not None) and isinstance(supermercado,Supermercado):
                if (nome_produto is not None) and isinstance (nome_produto, str):
                    if (descricao_produto is not None) and isinstance (descricao_produto, str):
                        self.__controlador_sistema.controlador_categoria.listar_categoria() # lista as categorias
                        categoria = self.__controlador_sistema.controlador_categoria.pega_codigo() # pega a categoria
                        if (categoria is not None) and isinstance(categoria, Categoria):
                            info_preco = self.__controlador_sistema.controlador_preco.incluir_novo_preco() #add preco
                            if (info_preco is not None) and isinstance(info_preco["valor"], float): #rever
                                qualificadores = self.__controlador_sistema.controlador_qualificador.inclui_qualificador() # adicina uma lista de qualificadores
                                for qualificador in qualificadores:
                                    if (qualificador is not None) and isinstance(qualificador, Qualificador):
                                            produto_existe = self.verifica_duplicidade_produto(nome_produto,categoria, supermercado, qualificadores)
                                            if produto_existe == False:
                                                codigo = self.gerar_codigo()
                                                if (codigo is not None) and isinstance(codigo, str):
                                                    novo_produto = Produto(nome_produto, descricao_produto, codigo, supermercado, categoria, qualificadores,usuario_logado) #add quem cadastrou
                                                    novo_produto.add_preco(info_preco)
                                                    self.__lista_produtos.append(novo_produto)
                                                    self.__tela_produto.mensagem_pro_usuario("Produto cadastrado com sucesso!")
                                                else:
                                                    self.__tela_produto.mensagem_pro_usuario("Não há codigos disponíveis")
                                            else:
                                                self.__tela_produto.mensagem_pro_usuario("Esse produto já existe")
                                    else:
                                        self.__tela_produto.mensagem_pro_usuario("Qualificador não aceito")
                            else:
                                self.__tela_produto.mensagem_pro_usuario("Valor do preço não é um numero de ponto flutuante")
                        else:
                            self.__tela_produto.mensagem_pro_usuario("Categoria do produto não encontrada")
                    else:
                        self.__tela_produto.mensagem_pro_usuario("Descrição do produto não aceita")
                else:
                    self.__tela_produto.mensagem_pro_usuario("Nome do produto não aceito")
            else:
                self.__tela_produto.mensagem_pro_usuario("Supermercado não encontrado")
        else:
            self.__tela_produto.mensagem_pro_usuario("Usuario não encontrado")
    
    def verifica_duplicidade_produto(self,nome, categoria, supermercado, qualificadores):
        produto_existe = False
        for produto in self.__lista_produtos:
            if produto.nome == nome:
                if produto.categoria.codigo == categoria.codigo:
                    if produto.supermercado == supermercado:
                        for qualificador in produto.qualificadores:
                            for novo_qualificador in qualificadores:
                                if qualificador.titulo == novo_qualificador.titulo:
                                    if qualificador.descricao == novo_qualificador.descricao:
                                        produto_existe = True
        return produto_existe

    def pesquisar_preco(self): 
        nome_produto = self.__tela_produto.pega_nome("Nome do produto: ")
        if (nome_produto is not None) and isinstance(nome_produto, str):
            for item in self.__lista_produtos:
                    if item.nome == nome_produto:
                        nome = item.nome
                        for qualificador in item.qualificadores:
                            lista = []
                            quali = qualificador.titulo+":"+qualificador.descricao
                            lista.append(quali)
                        qualificador1 = lista
                        preco = item.confirmacoes.valor
                        mercado = item.supermercado.nome
                        info = {"nome": nome,"qualificador": qualificador1, "preco": preco, "mercado": mercado}
                        self.__tela_produto.mostra_resultados_busca(info)
        else:
            self.__tela_produto.mensagem_pro_usuario("Nome do produto não é válido!")

    def lancar_preco(self):
        produto_existe = False
        mercado = self.__tela_produto.pega_nome("Nome do mercado: ")
        supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(mercado)
        if (supermercado is not None) and isinstance(supermercado,Supermercado):
            self.__controlador_sistema.controlador_categoria.listar_categoria() #lista as categorias
            categoria = self.__controlador_sistema.controlador_categoria.pega_codigo() # pega a categoria
            nome_produto = self.__tela_produto.pega_nome("Nome do produto: ")
            qualificadores = self.__controlador_sistema.controlador_qualificador.inclui_qualificador() # adicina uma lista de qualificadores
            produto_existe = self.verifica_duplicidade_produto(nome_produto, categoria, supermercado, qualificadores)
            if produto_existe == True:
                info_preco = self.__controlador_sistema.controlador_preco.incluir_novo_preco()
                for produto in self.__lista_produtos:
                    if nome_produto == produto.nome:
                        if produto.supermercado == supermercado:
                            if produto.categoria == categoria:
                                produto.add_preco(info_preco)
                                self.__tela_produto.mensagem_pro_usuario("Novo preço lançado")
            else:
                self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")
                            #compara o preço e entao confirma ou adiciona um novo
        else:
                self.__tela_produto.mensagem_pro_usuario("Mercado não encontrado")

    def excluir_produto(self):
        mercado = self.__tela_produto.pega_nome("---Excluir Produto--- \n Nome do mercado: ")  #testar caixa vazia
        supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(mercado)
        if (supermercado is not None) and isinstance(supermercado,Supermercado):
            nome = self.__tela_produto.pega_nome("Nome do produto: ")
            if (nome is not None) and isinstance(nome,str):
                categoria = self.__controlador_sistema.controlador_categoria.pega_codigo()
                codigo = self.__tela_produto.pega_nome("Codigo do produto: ")
                if (codigo is not None) and isinstance(codigo,str):
                    for produto in self.__lista_produtos:
                        if produto.supermercado == supermercado:
                            if produto.nome == nome:
                                if produto.categoria == categoria:
                                    if produto.codigo == codigo:
                                            self.__lista_produtos.remove(produto)
                                            self.__tela_produto.mensagem_pro_usuario("Produto Excluido com Sucesso")
                                    else:
                                            self.__tela_produto.mensagem_pro_usuario("Não foi possivel excluir o produto") 
                else:
                    self.__tela_produto.mensagem_pro_usuario("Código inváido")    
            else:
                self.__tela_produto.mensagem_pro_usuario("Nenhum produto encontrado")
        else:
            self.__tela_produto.mensagem_pro_usuario("Supermercado não encontrado")

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
        nome_mercado = self.__tela_produto.pega_nome("Nome do Mercado: ")
        supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(nome_mercado)
        if (supermercado is not None) and isinstance(supermercado,Supermercado):
                for item in self.__lista_produtos:
                    if item.supermercado == supermercado:
                        nome = item.nome
                        preco = item.confirmacoes.valor
                        categoria = item.categoria.descricao
                        codigo = item.codigo
                        info = {"nome": nome, "preco": preco, "categoria": categoria, "codigo": codigo}
                        self.__tela_produto.produtos_por_mercado(info)
        else:
            self.__tela_produto.mensagem_pro_usuario("Mercado não encontrado")

    def evolucao_precos(self):
        pass
        #nome_mercado = self.__tela_produto.pega_nome("Nome do mercado")
        #supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(nome_mercado)
        #if (supermercado is not None) and isinstance(supermercado,Supermercado):
            #nome_produto = self.__tela_produto.pega_nome("Nome do Produto")
            #if (nome_produto is not None) and isinstance(nome_produto, str):
                #for produto in self.__lista_produtos:
                    #if produto.nome == nome_produto:
                        #if produto.supermercado == supermercado:
                            #for preco in produto.lista_precos:
                                #info = {"Data": preco.postagem, "Valor": preco.valor}

    def gerar_codigo(self):
        existe  = False
        codigo = randint(0, 500)
        codigo = str(codigo)
        for produto in self.__lista_produtos:
            if codigo == produto.codigo:
                existe = True
        if existe == False:
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

