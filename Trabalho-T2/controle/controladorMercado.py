from entidade.supermercado import Supermercado
from limite.tela_supermercado import TelaSupermercado


class ControladorMercado:
    def __init__(self, controladorSistema):
        self.__lista_supermercados = {}
        self.__telaSupermercado = TelaSupermercado()
        self.__controladorSistema = controladorSistema

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
                    self.__lista_supermercados.pop(mercado)
                    mercado = Supermercado(novos_dados_mercado["nome"], novos_dados_mercado["endereco"], dono)
                    if novos_dados_mercado["endereco"] not in self.__lista_supermercados and novos_dados_mercado["nome"] not in self.__lista_supermercados:
                        self.__lista_supermercados[novos_dados_mercado["nome"]] = mercado
                        self.__telaSupermercado.mensagem_pro_usuario("Dados Alterados Com Sucesso Com Sucesso")
                    else:
                        self.__telaSupermercado.mensagem_pro_usuario("Erro: Ja existe um supermercado com esses dados")
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
