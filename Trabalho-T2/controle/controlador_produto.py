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


class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__lista_produtos = []
        self.__usuarios_tempo = {}
        self.__usuario = None

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    def cadastrar_produto(self):
        pega_dados = self.__tela_produto.pega_dados()  # pega nome,descrição e mercado  do produto
        supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(pega_dados["mercado"])
        if (supermercado is not None) and isinstance(supermercado, Supermercado):
            verificar = self.verifica_supermercado(supermercado)
            if verificar == True:
                self.__controlador_sistema.controlador_categoria.listar_categoria()  # lista as categorias
                categoria = self.__controlador_sistema.controlador_categoria.pega_codigo()  # pega a categoria
                if (categoria is not None) and isinstance(categoria, Categoria):
                    if (pega_dados["preco"] is not None) and isinstance(pega_dados["preco"], float):  # rever
                        qualificadores = self.__controlador_sistema.controlador_qualificador.inclui_qualificador()  # adicina uma lista de qualificadores
                        produto_existe = self.verifica_duplicidade_produto(pega_dados["nome_produto"], categoria,
                                                                           supermercado, qualificadores)
                        if produto_existe == None:
                            codigo = self.gerar_codigo()
                            novo_produto = Produto(pega_dados["nome_produto"], pega_dados["descricao"], codigo,
                                                   supermercado, categoria, qualificadores, self.__usuario)
                            novo_produto.add_preco(pega_dados["preco"])
                            self.__lista_produtos.append(novo_produto)
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
            if supermercado.dono == self.__usuario.email:
                verificar = True
        return verificar

    def verifica_duplicidade_produto(self, nome, categoria, supermercado, qualificadores):  # revisar
        for produto in self.__lista_produtos:
            if produto.nome == nome:
                if produto.categoria == categoria:  # categoria.codigo
                    if produto.supermercado == supermercado:
                        for qualificador in produto.qualificadores:  # verificar os qualificadores
                            for novo_qualificador in qualificadores:
                                if qualificador.titulo == novo_qualificador.titulo:
                                    if qualificador.descricao == novo_qualificador.descricao:
                                        return produto
        return None

    def pega_produto_por_codigo(self, codigo: int):
        for produto in self.__lista_produtos:
            if (produto.codigo == codigo):
                return produto
        return None

    def pesquisar_preco(self):
        # buscar pelo nome do produto com ou sem qualificadores
        # ordenar os resultados por preço, número de confirmações ou por data de postagem.
        nome_produto = self.__tela_produto.pega_nome("Nome do produto: ")
        if (nome_produto is not None) and isinstance(nome_produto, str):
            for item in self.__lista_produtos:
                if item.nome == nome_produto:
                    nome = item.nome
                    for qualificador in item.qualificadores:
                        lista = []
                        quali = qualificador.titulo + ":" + qualificador.descricao
                        lista.append(quali)
                    qualificador1 = lista
                    preco = item.confirmacoes.valor
                    mercado = item.supermercado.nome
                    info = {"nome": nome, "qualificador": qualificador1, "preco": preco, "mercado": mercado}
                    self.__tela_produto.mostra_resultados_busca(info)
        else:
            self.__tela_produto.mensagem_pro_usuario("Nome do produto não é válido!")

    def lancar_preco(self):
        # pegar o usuario logado para associar ao produto
        # depois aponta o preço com duas casas decimais, e confirma ou lança novo preço
        # Um usuário somente poderá atualizar/cadastrar o preço de um determinado produto uma vez por dia.
        mercado = self.__tela_produto.pega_nome("Nome do mercado: ")  # seleciona o supermercado
        supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(mercado)
        dia = timedelta(days=1)
        if (supermercado is not None) and isinstance(supermercado, Supermercado):
            verificar = self.verifica_supermercado(supermercado)
            if verificar == True:
                self.__controlador_sistema.controlador_categoria.listar_categoria()  # lista as categorias
                categoria = self.__controlador_sistema.controlador_categoria.pega_codigo()  # #seleciona a categoria
                nome_produto = self.__tela_produto.pega_nome("Nome do produto: ")  # seleciona o nome do produto
                qualificadores = self.__controlador_sistema.controlador_qualificador.inclui_qualificador()  # adicina uma lista de qualificadores
                pega_produto = self.verifica_duplicidade_produto(nome_produto, categoria, supermercado, qualificadores)
                if (pega_produto is not None) and isinstance(pega_produto, Produto):
                    if pega_produto.usuario not in self.__usuarios_tempo:
                        novo_preco = self.__tela_produto.pega_preço()
                        pega_produto.add_preco(novo_preco)  # confirma ou adiciona  talaez retornar uma msg
                        self.adicionar_registro(pega_produto, novo_preco, "inclusão")
                        self.__tela_produto.mensagem_pro_usuario("Novo preço de " + str(novo_preco) + " lançado")
                        self.__usuarios_tempo[pega_produto.usuario] = datetime.date.today()
                    else:
                        if (datetime.date.today() - self.__usuarios_tempo[pega_produto.usuario]) >= dia:
                            novo_preco = self.__tela_produto.pega_preço()
                            pega_produto.add_preco(novo_preco)  # confirma ou adiciona  talaez retornar uma msg
                            self.adicionar_registro(pega_produto, novo_preco, "inclusão")
                            self.__tela_produto.mensagem_pro_usuario("Novo preço de " + str(novo_preco) + " lançado")
                            self.__usuarios_tempo[pega_produto.usuario] = datetime.date.today()
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
        codigo_produto = self.__tela_produto.pega_inteiro("Digite o codigo do produto: ")
        produto = self.pega_produto_por_codigo(str(codigo_produto))
        if (produto is not None):
            self.__lista_produtos.remove(produto)
            self.__tela_produto.mensagem_pro_usuario("Produto excluido com sucesso")
        else:
            self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")

    def registros_de_um_produto(self):
        # Registros (inclusão, exclusão, alteração e listagem) de preços de produtos
        codigo_produto = self.__tela_produto.pega_inteiro("Digite o codigo do produto: ")
        produto = self.pega_produto_por_codigo(str(codigo_produto))
        if (produto is not None):
            for registro in produto.registros:
                self.__tela_produto.mensagem_pro_usuario("Produto: " + produto.nome)
                self.__tela_produto.mostra_registros({"data": registro["data"],
                                                      "operacao": registro["operacao"],
                                                      "valor": registro["valor"]})
        else:
            self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")

    def adicionar_registro(self, produto, valor, msg):
        data = datetime.date.today()
        novo_registro = {"data": data, "operacao": msg, "valor": valor}
        produto.registros.append(novo_registro)

    def relatorio(self):
        # evolução dos preços de um produto por data, com valor mais caro e mais barato já registrado
        lista_opcoes = {1: self.produtos_por_supermercado, 2: self.evolucao_precos, 3: self.listar_precos_de_um_produto,
                        0: self.abre_tela}
        while True:
            opcao_escolhida = self.__tela_produto.relatorios()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def produtos_por_supermercado(self):
        nome_mercado = self.__tela_produto.pega_nome("Nome do Mercado: ")
        supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(nome_mercado)
        if (supermercado is not None) and isinstance(supermercado, Supermercado):
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
        # nome_mercado = self.__tela_produto.pega_nome("Nome do mercado")
        # supermercado = self.__controlador_sistema.controladorMercado.retorna_supermercado(nome_mercado)
        # if (supermercado is not None) and isinstance(supermercado,Supermercado):
        # nome_produto = self.__tela_produto.pega_nome("Nome do Produto")
        # if (nome_produto is not None) and isinstance(nome_produto, str):
        # for produto in self.__lista_produtos:
        # if produto.nome == nome_produto:
        # if produto.supermercado == supermercado:
        # for preco in produto.lista_precos:
        # info = {"Data": preco.postagem, "Valor": preco.valor}

    def excluir_preco(self):
        # pega o codigo do produto e lista os preços e exclui um deles
        codigo_produto = self.__tela_produto.pega_inteiro("Digite o codigo do produto: ")
        produto = self.pega_produto_por_codigo(str(codigo_produto))
        if (produto is not None):
            self.__tela_produto.mensagem_pro_usuario("Lista de preços do produto")
            for preco in produto.lista_precos:
                valor = str(preco.valor)
                self.__tela_produto.mensagem_pro_usuario("R$" + valor)
            preco_excluir = self.__tela_produto.pega_float(
                "Digite o preço para excluir: ")  # pegar com duas casas decimais
            if (preco_excluir is not None):
                for preco1 in produto.lista_precos:
                    if preco_excluir == preco1.valor:
                        produto.lista_precos.remove(preco1)
                        self.adicionar_registro(produto, preco_excluir, "Exclusão")
                        self.__tela_produto.mensagem_pro_usuario("Preço excluido com sucesso")
                    else:
                        self.__tela_produto.mensagem_pro_usuario("Preço não encontrado")
        else:
            self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")

    def alterar_preco(self):
        # pega o codigo do produto e lista os preços e altera um deles
        # pensando o que faz sentido alterar
        pass

    def listar_precos_de_um_produto(self):
        codigo_produto = self.__tela_produto.pega_inteiro("Digite o codigo do produto: ")
        produto = self.pega_produto_por_codigo(str(codigo_produto))
        if (produto is not None):
            for preco in produto.lista_precos:
                valor = str(preco.valor)
                self.__tela_produto.mensagem_pro_usuario("R$" + valor)
        else:
            self.__tela_produto.mensagem_pro_usuario("Produto não encontrado")

    def gerar_codigo(self):
        existe = False
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
        lista_opcoes = {1: self.cadastrar_produto, 2: self.pesquisar_preco, 3: self.lancar_preco,
                        4: self.excluir_produto,
                        5: self.registros_de_um_produto, 6: self.relatorio, 7: self.excluir_preco, 0: self.retornar}

        while True:
            opcoes = self.__tela_produto.telaopcoes()
            funcao_escolhida = lista_opcoes[opcoes]
            funcao_escolhida()
