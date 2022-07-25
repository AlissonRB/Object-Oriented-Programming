from entidade.supermercado import Supermercado
from limite.telaSupermercado import TelaSupermercado
from DAOs.mercado_dao import MercadoDAO


class ControladorMercado:
    def __init__(self, controladorSistema):
        self.__mercado_Dao = MercadoDAO()
        self.__telaSupermercado = TelaSupermercado()
        self.__controladorSistema = controladorSistema

    def pega_supermercado(self, nome):
        for mercado in self.__mercado_Dao.get_all():
            if mercado.nome == nome:
                return mercado
        return None

    def retorna_supermercado(self, nome):  # retorna objeto
        for mercado in self.__mercado_Dao.get_all():
            if mercado.nome == nome:
                return mercado
        return None

    def cadastrar_supermercado(self):
        typed = self.__telaSupermercado.pega_dados_supermercado()
        dono = self.__controladorSistema.cria_dono()
        if dono is not None:
            mercado = Supermercado(typed["nome"], typed["endereco"], dono)
            verificar_nome = self.__mercado_Dao.get(typed['nome'])
            if verificar_nome == None:
                self.__mercado_Dao.add(mercado)
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
            if mercado is not None:
                novos_dados_mercado = self.__telaSupermercado.pega_dados_supermercado()
                self.__mercado_Dao.remove(mercado.nome)
                mercado = Supermercado(novos_dados_mercado["nome"], novos_dados_mercado["endereco"], dono)
                verificar_nome = self.__mercado_Dao.get(typed['nome'])
                if verificar_nome == None:
                    self.__mercado_Dao.add(mercado)
                    self.__telaSupermercado.mensagem_pro_usuario("Dados Alterados Com Sucesso Com Sucesso")
                else:
                    self.__telaSupermercado.mensagem_pro_usuario("Erro: Ja existe um supermercado com esses dados")
            else:
                self.__telaSupermercado.mensagem_pro_usuario("Dados Incorretos")
        else:
            self.__telaSupermercado.mensagem_pro_usuario("Dono Inexistente")

    def exclui_supermercado(self):
        typed = self.__telaSupermercado.seleciona_mercado()
        mercado = self.pega_supermercado(typed["nome"])
        dono = self.__controladorSistema.cria_dono()
        if dono is not None:
            if (dono.email == mercado.dono.email):
                if mercado is not None:
                    self.__mercado_Dao.remove(mercado.nome)
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
            self.__telaSupermercado.mensagem_pro_usuario(f"{mercado.nome}"
                                                         f" {mercado.endereco}"
                                                         f" {mercado.dono.nome}")
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
