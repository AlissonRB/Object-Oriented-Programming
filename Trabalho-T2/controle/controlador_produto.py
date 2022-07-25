from entidade.qualificador import Qualificador
from limite.tela_produto import TelaProduto
from entidade.categoria import Categoria
from entidade.supermercado import Supermercado
from entidade.produto import Produto
from entidade.usuarioFisico import UsuarioFisico
from entidade.usuarioJuridico import UsuarioJuridico
from random import randint
import datetime
from datetime import timedelta
from DAOs.produtos_dao import ProdutoDAO


class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__produto_DAO = ProdutoDAO()
        self.__usuarios_tempo = {}
        self.__usuario = None

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    def cadastrar_produto(self):
        descricao_categoria = self.__controlador_sistema.controlador_categoria.retorna_nomes_categorias()
        descricao_mercado = self.__controlador_sistema.controladorMercado.retorna_nomes_mercado()
        pega_dados = self.__tela_produto.pega_dados(descricao_categoria, descricao_mercado)  # pega nome,descrição e mercado  do produto
        if pega_dados is not None:
            mercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(pega_dados["mercado"])
            if (mercado is not None) and isinstance(mercado, Supermercado):
                verificar = self.verifica_supermercado(mercado)
                if verificar == True:
                    categoria = self.__controlador_sistema.controlador_categoria.pega_categoria_por_descricao(pega_dados["categoria"])  # pega a categoria
                    if (categoria is not None) and isinstance(categoria, Categoria):
                        if (pega_dados["preco"] is not None) and isinstance(pega_dados["preco"], float):  # rever para flutuante
                            qualificadores = self.__controlador_sistema.controlador_qualificador.inclui_qualificador()  # adicina uma lista de qualificadores
                            produto_existe = self.verifica_existencia_produto(pega_dados["nome"], mercado)
                            if produto_existe == None:
                                    codigo = self.gerar_codigo()
                                    novo_produto = Produto(pega_dados["nome"], pega_dados["descricao"], codigo,
                                                        mercado, categoria, qualificadores, self.__usuario)
                                    novo_produto.add_preco(pega_dados["preco"])
                                    self.adicionar_registro(novo_produto, pega_dados["preco"], "inclusão")
                                    self.__produto_DAO.add(novo_produto)
                                    self.adicionar_registro(novo_produto, pega_dados["preco"], "inclusão")
                                    self.__tela_produto.mensagem_pro_usuario("Produto cadastrado com sucesso!")
                            else:
                                    self.__tela_produto.mensagem_pro_usuario("Esse produto já existe")
                        else:
                            self.__tela_produto.mensagem_pro_usuario("Valor do preço não aceito")
                    else:
                        self.__tela_produto.mensagem_pro_usuario("Categoria do produto não encontrada")
                else:
                    self.__tela_produto.mensagem_pro_usuario("Usuario Juridico não pode alterar em outros supermercados")
            else:
                self.__tela_produto.mensagem_pro_usuario("Supermercado não encontrado")

    def verifica_supermercado(self,
                              supermercado):  # verifica se o supermercado está associado a conta de usuario juridico
        verificar = False
        if isinstance(self.__usuario, UsuarioFisico):
            verificar = True
        if isinstance(self.__usuario, UsuarioJuridico):
            if supermercado.dono.nome == self.__usuario.nome:
                verificar = True
        return verificar

    def verifica_existencia_produto(self, nome, supermercado):
        for produto in self.__produto_DAO.get_all():
            if produto.nome == nome:
                if produto.supermercado.nome == supermercado.nome:
                    return produto
        return None

    def pega_produto_por_codigo(self, codigo: int):
        for produto in self.__produto_DAO.get_all():
            if (produto.codigo == codigo):
                return produto
        return None

    def pesquisar_preco(self):
        info = []
        nome_produto = self.__tela_produto.pesquisar_preco()
        if nome_produto is not None:
            if isinstance(nome_produto['nome'], str):
                for item in self.__produto_DAO.get_all():
                    if item.nome == nome_produto['nome']:
                        nome = item.nome
                        for qualificador in item.qualificadores:
                            lista = []
                            quali = qualificador.titulo + ":" + qualificador.descricao
                            lista.append(quali)
                        qualificador1 = lista
                        preco = item.confirmacoes.valor
                        mercado = item.supermercado.nome
                        info.append({"nome": nome, "qualificador": qualificador1, "preco": preco, "mercado": mercado})
                if len(info) == 0:
                    self.__tela_produto.mensagem_pro_usuario("Nenhum produto encontrado !")
                else:
                    self.__tela_produto.mostra_resultados_busca(info)
            else:
                self.__tela_produto.mensagem_pro_usuario("Nome do produto não é válido!")

    def lancar_preco(self):
        descricao_categoria = self.__controlador_sistema.controlador_categoria.retorna_nomes_categorias()
        descricao_mercado = self.__controlador_sistema.controladorMercado.retorna_nomes_mercado()
        lancar = self.__tela_produto.lancamento_preco(descricao_categoria, descricao_mercado) #retorna mercado, categoria, nome e preço
        if lancar is not None:
            supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(lancar['supermercado'])
            dia = timedelta(days=1)
            if (supermercado is not None) and isinstance(supermercado, Supermercado):
                verificar = self.verifica_supermercado(supermercado)
                if verificar == True:
                    #categoria = self.__controlador_sistema.controlador_categoria.pega_categoria_por_descricao(lancar["categoria"])  # #seleciona a categoria
                    nome_produto = lancar['nome']  # seleciona o nome do produto
                    verificar_produto = self.verifica_existencia_produto(nome_produto, supermercado)
                    if (verificar_produto is not None) and isinstance(verificar_produto, Produto):
                        if verificar_produto.usuario not in self.__usuarios_tempo:
                            verificar_produto.add_preco(lancar['preco'])
                            self.adicionar_registro(verificar_produto, lancar['preco'], "inclusão")
                            self.__usuarios_tempo[verificar_produto.usuario] = datetime.date.today()
                            self.__produto_DAO.update(verificar_produto)
                            self.__tela_produto.mensagem_pro_usuario('Novo preço lançado com sucesso')
                    else:
                        if (datetime.date.today() - self.__usuarios_tempo[verificar_produto.usuario]) >= dia:
                            novo_preco = lancar['preco']#self.__tela_produto.pega_preço()
                            verificar_produto.add_preco(novo_preco)
                            self.adicionar_registro(verificar_produto, novo_preco, "inclusão")
                            self.__tela_produto.mensagem_pro_usuario("Novo preço de " + str(novo_preco) + " lançado")
                            self.__usuarios_tempo[verificar_produto.usuario] = datetime.date.today()
                        else:
                            self.__tela_produto.mensagem_pro_usuario(
                                "Voce deve esperar um dia para poder alterar novamente o preco de um produto")
                else:
                    self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")
            else:
                self.__tela_produto.mensagem_pro_usuario("Usuario Juridico não pode alterar em outros supermercados")
        else:
            self.__tela_produto.mensagem_pro_usuario("Supermercado não encontrado")

    def excluir_produto(self):
        codigo_produto = self.__tela_produto.pega_inteiro()
        if codigo_produto is not None:
            produto = self.pega_produto_por_codigo(str(codigo_produto))
            if (produto is not None):
                mercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(produto.supermercado.nome)
                verificar = self.verifica_supermercado(mercado)
                if verificar == True:
                    self.__produto_DAO.remove(produto.codigo)
                    self.__tela_produto.mensagem_pro_usuario("Produto excluido com sucesso")
                else:
                    self.__tela_produto.mensagem_pro_usuario("Usuario Juridico não pode alterar em outros supermercados")
            else:
                self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")

    def registros_de_um_produto(self):
        # Registros (inclusão, exclusão, alteração e listagem) de preços de produtos
        info = []
        codigo_produto = self.__tela_produto.pega_inteiro()
        if codigo_produto is not None:
            produto = self.pega_produto_por_codigo(str(codigo_produto))#lista de dicionarios com o mostra resutados de busca
            if (produto is not None) and isinstance(produto, Produto):
                for registro in produto.registros:
                    info.append({"data": registro["data"],
                                "operacao": registro["operacao"],
                                "valor": registro["valor"],
                                "usuario": registro["usuario"]})
                self.__tela_produto.mostra_registros(info)
            else:
                self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")

    def adicionar_registro(self, produto, valor, msg):
        data = datetime.date.today()
        novo_registro = {"data": data, "operacao": msg, "valor": valor, "usuario": self.__usuario.nome}
        produto.registros.append(novo_registro)

    def relatorio(self):
        # evolução dos preços de um produto por data, com valor mais caro e mais barato já registrado
        lista_opcoes = {1: self.produtos_por_supermercado, 2: self.listar_precos_de_um_produto,
                        0: self.abre_tela}
        while True:
            opcao_escolhida = self.__tela_produto.relatorios()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def produtos_por_supermercado(self):
        lista_produtos = []
        descricao_mercado = self.__controlador_sistema.controladorMercado.retorna_nomes_mercado() #retorna umalista de nomes de mercado
        nome_mercado = self.__tela_produto.pega_nome(descricao_mercado)
        supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(nome_mercado)
        if (supermercado is not None) and isinstance(supermercado, Supermercado):
            for item in self.__produto_DAO.get_all():
                    mercado = item.supermercado.nome
                    nome1 = item.nome
                    preco = item.confirmacoes.valor
                    categoria = item.categoria.nome
                    codigo = item.codigo
                    if mercado == supermercado.nome:
                        lista_produtos.append({"nome": nome1, "preco": preco, "categoria": categoria, "codigo": codigo})
            self.__tela_produto.produtos_por_mercado(lista_produtos)
        else:
            self.__tela_produto.mensagem_pro_usuario("Mercado não encontrado")

    def listar_precos_de_um_produto(self):
        info = []
        codigo_produto = self.__tela_produto.pega_inteiro()
        if codigo_produto is not None:
            produto = self.pega_produto_por_codigo(str(codigo_produto))
            if (produto is not None):
                for preco in produto.lista_precos:
                    info.append(preco.valor)
                self.__tela_produto.precos_produto(produto.nome, info)
            else:
                self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")

    def gerar_codigo(self):
        existe = False
        codigo = randint(0, 500)
        codigo = str(codigo)
        for produto in self.__produto_DAO.get_all():
            if codigo == produto.codigo:
                existe = True
        if existe == False:
            return codigo
        else:
            return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_produto, 2: self.pesquisar_preco, 3: self.lancar_preco,
                        4: self.excluir_produto,
                        5: self.registros_de_um_produto, 6: self.relatorio, 0: self.retornar}

        while True:
            opcoes = self.__tela_produto.telaopcoes()
            funcao_escolhida = lista_opcoes[opcoes]
            funcao_escolhida()