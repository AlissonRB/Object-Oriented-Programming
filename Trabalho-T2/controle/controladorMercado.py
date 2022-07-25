from entidade.supermercado import Supermercado
from limite.telaSupermercado import TelaSupermercado


class ControladorMercado:
    def __init__(self, controladorSistema):
        self.__lista_supermercados = {}
        self.__telaSupermercado = TelaSupermercado()
        self.__controladorSistema = controladorSistema
        #testes
        dono = self.__controladorSistema.controladorUsuario.user_juridico
        self.mercado1 = Supermercado("ABC", "rua", dono)
        self.__lista_supermercados["ABC"] = self.mercado1
        dono2 = self.__controladorSistema.controladorUsuario.user_juridico2
        self.mercado2 = Supermercado("BIG", "rua", dono2)
        self.__lista_supermercados["BIG"] = self.mercado2

    @property
    def lista_supermercados(self):
        return self.__lista_supermercados

    @lista_supermercados.setter
    def lista_supermercados(self, lista_supermercados):
        self.__lista_supermercados = lista_supermercados

    def pega_supermercado(self, nome):
        for mercado in self.__lista_supermercados:
            if mercado == nome:
                return mercado
        return None
    
    def retorna_supermercado(self,nome):
        for mercado in self.__lista_supermercados:
            if mercado == nome:
                return self.__lista_supermercados[mercado]
    
    def retorna_nomes_mercado(self):
        nomes = []
        for mercado in self.__lista_supermercados:
            nomes.append(mercado)
        return nomes

    def cadastrar_supermercado(self):
        typed = self.__telaSupermercado.pega_dados_supermercado()
        dono = self.__controladorSistema.cria_dono()
        if dono is not None:
            mercado = Supermercado(typed["nome"], typed["endereco"], dono)
            if typed["endereco"] not in self.__lista_supermercados and typed["nome"] not in self.__lista_supermercados:
                self.__lista_supermercados[typed["nome"]] = mercado
                self.__telaSupermercado.mensagem_pro_usuario("Cadastrado Com Sucesso")
                self.__controladorSistema.abre_tela()
            else:
                self.__telaSupermercado.mensagem_pro_usuario("Supermercado Ja Cadastrado")
        else:
            self.__telaSupermercado.mensagem_pro_usuario("Pessoa Juridica Inexistente")

    def alterar_supermercado(self):
        typed = self.__telaSupermercado.seleciona_mercado()
        mercado = self.pega_supermercado(typed["nome"])
        dono = self.__controladorSistema.cria_dono()
        if dono is not None:
            if dono == self.__lista_supermercados[mercado].dono:
                if mercado is not None:
                    novos_dados_mercado = self.__telaSupermercado.pega_dados_supermercado()
                    self.__lista_supermercados[mercado].nome = novos_dados_mercado["nome"]
                    self.__lista_supermercados[mercado].endereco = novos_dados_mercado["endereco"]
                    self.__lista_supermercados[mercado].dono = dono
                    self.__telaSupermercado.mensagem_pro_usuario("Dados Alterados Com Sucesso")
                else:
                    self.__telaSupermercado.mensagem_pro_usuario("Mercado Nao Encontrado")
            else:
                self.__telaSupermercado.mensagem_pro_usuario("Dados do Dono Incorretos")
        else:
            self.__telaSupermercado.mensagem_pro_usuario("Dono Inexistente")

    def exclui_supermercado(self):
        typed = self.__telaSupermercado.seleciona_mercado()
        mercado = self.pega_supermercado(typed["nome"])
        dono = self.__controladorSistema.cria_dono()
        if dono is not None:
            if dono == self.__lista_supermercados[mercado].dono:
                if mercado is not None:
                    self.__lista_supermercados.pop(mercado)
                    self.__telaSupermercado.mensagem_pro_usuario("Mercado Removido com Sucesso")
                else:
                    self.__telaSupermercado.mensagem_pro_usuario("ATENCAO: Mercado não existente")
            else:
                self.__telaSupermercado.mensagem_pro_usuario("Dados do dono incorretos")
        else:
            self.__telaSupermercado.mensagem_pro_usuario("Dono nao Existente")

    def listar_mercado(self):
        typed = self.__telaSupermercado.seleciona_mercado()
        mercado = self.pega_supermercado(typed["nome"])
        if mercado is not None:
            self.__telaSupermercado.mensagem_pro_usuario(f"{self.__lista_supermercados[mercado].nome}"
                                                         f" {self.__lista_supermercados[mercado].endereco}"
                                                         f" {self.__lista_supermercados[mercado].dono}")
        else:
            self.__telaSupermercado.mensagem_pro_usuario("ATENCAO: Mercado não existente")

    def retornar(self):
        self.__controladorSistema.abre_tela()

    def abretela(self):
        lista_opcoes = {1: self.cadastrar_supermercado, 2: self.alterar_supermercado, 3: self.exclui_supermercado,
                        4: self.listar_mercado, 0: self.retornar}

        while True:
            opcao_escolhida = self.__telaSupermercado.telaopcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
