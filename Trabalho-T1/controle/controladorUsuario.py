from limite.telaUsuario import TelaUsuario
from entidade.usuarioFisico import UsuarioFisico
from entidade.usuarioJuridico import UsuarioJuridico


class ControladorUsuario:

    def __init__(self, controladorSistema):
        self.__usuariosfisicos = {}
        self.__usuariosjuridicos = {}
        self.__telaUsuario = TelaUsuario()
        self.__controladorSistema = controladorSistema

    @property
    def usuariosfisicos(self):
        return self.__usuariosfisicos

    @property
    def usuariosjuridicos(self):
        return self.__usuariosjuridicos

    @usuariosfisicos.setter
    def usuariosfisicos(self, usuariosfisicos):
        self.__usuariosfisicos = usuariosfisicos

    @usuariosjuridicos.setter
    def usuariosjuridicos(self, usuariosjuridicos):
        self.__usuariosjuridicos = usuariosjuridicos

    def pega_usuario_juridico(self, email: str):
        for usuario_juridico in self.__usuariosjuridicos:
            if usuario_juridico == email:
                return usuario_juridico
        return None

    def pega_usario_fisico(self, email: str):
        for usario_fisico in self.__usuariosfisicos:
            if usario_fisico == email:
                return usario_fisico
        return None

    def realizaloginfisico(self):
        typed = self.__telaUsuario.tela_login_fisica()
        if typed["email"] in self.__usuariosfisicos:
            if self.__usuariosfisicos[typed["email"]].cpf == typed["cpf"]:
                self.__telaUsuario.mensagem_pro_usuario("Seja bem vindo!")
                self.__controladorSistema.abre_tela()
            else:
                self.__telaUsuario.mensagem_pro_usuario("Informações de login incorretas!")
        else:
            self.__telaUsuario.mensagem_pro_usuario("Informações de login incorretas!")

    def realizaloginjuridico(self):
        typed = self.__telaUsuario.tela_login_juridica()
        if typed["email"] in self.__usuariosjuridicos:
            if self.__usuariosjuridicos[typed["email"]].cnpj == typed["cnpj"]:
                self.__telaUsuario.mensagem_pro_usuario("Seja bem vindo!")
                self.__controladorSistema.abre_tela()
            else:
                self.__telaUsuario.mensagem_pro_usuario("Informações de login incorretas!")
        else:
            self.__telaUsuario.mensagem_pro_usuario("Informações de login incorretas!")

    def cadastrar_pessoa_juridica(self):
        typed = self.__telaUsuario.pega_dados_conta_juridica()
        pessoa_juridica = UsuarioJuridico(typed["nome"], typed["email"], typed["cnpj"])
        if typed["email"] not in self.__usuariosjuridicos and typed["cnpj"] not in self.__usuariosjuridicos:
            self.__usuariosjuridicos[typed["email"]] = pessoa_juridica
            self.__telaUsuario.mensagem_pro_usuario("Cadastrado Com Sucesso")
            self.__controladorSistema.abre_tela()
        else:
            self.__telaUsuario.mensagem_pro_usuario("Usuario Ja Cadastrado")

    def cadastrar_pessoa_fisica(self):
        typed = self.__telaUsuario.pega_dados_conta_fisica()
        pessoa_fisica = UsuarioFisico(typed["nome"], typed["email"], typed["cpf"])
        if typed["email"] not in self.__usuariosfisicos and typed["cpf"] not in self.__usuariosfisicos:
            self.__usuariosfisicos[typed["email"]] = pessoa_fisica
            self.__telaUsuario.mensagem_pro_usuario("Cadastrado Com Sucesso")
            self.__controladorSistema.abre_tela()
        else:
            self.__telaUsuario.mensagem_pro_usuario("Usuario Ja Cadastrado")

    def alterar_conta_fisica(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usario_fisico(typed["email"])
        if usuario is not None:
            novos_dados_usuario = self.__telaUsuario.pega_dados_conta_fisica()
            self.__usuariosfisicos[usuario].nome = novos_dados_usuario["nome"]
            self.__usuariosfisicos[usuario].email = novos_dados_usuario["email"]
            self.__usuariosfisicos[usuario].cpf = novos_dados_usuario["cpf"]
            self.__telaUsuario.mensagem_pro_usuario("Dados Alterados Com Sucesso")
        else:
            self.__telaUsuario.mensagem_pro_usuario("ATENCAO: Usuario não existente")

    def alterar_conta_juridica(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usuario_juridico(typed["email"])
        if usuario is not None:
            novos_dados_usuario = self.__telaUsuario.pega_dados_conta_juridica()
            self.__usuariosjuridicos[usuario].nome = novos_dados_usuario["nome"]
            self.__usuariosjuridicos[usuario].email = novos_dados_usuario["email"]
            self.__usuariosjuridicos[usuario].cnpj = novos_dados_usuario["cnpj"]
            self.__telaUsuario.mensagem_pro_usuario("Dados Alterados Com Sucesso")
        else:
            self.__telaUsuario.mensagem_pro_usuario("ATENCAO: Usuario não existente")

    def excluir_conta_fisica(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usario_fisico(typed["email"])
        if usuario is not None:
            self.__usuariosfisicos.pop(usuario)
            self.__telaUsuario.mensagem_pro_usuario("Usuario Removido com Sucesso")
        else:
            self.__telaUsuario.mensagem_pro_usuario("ATENCAO: Usuario não existente")

    def excluir_conta_juridica(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usuario_juridico(typed["email"])
        if usuario is not None:
            self.__usuariosjuridicos.pop(usuario)
            self.__telaUsuario.mensagem_pro_usuario("Usuario Removido com Sucesso")
        else:
            self.__telaUsuario.mensagem_pro_usuario("ATENCAO: Usuario não existente")

    def verifica_usuario_juridico(self):
        typed = self.__telaUsuario.tela_login_juridica()
        dono = self.pega_usuario_juridico(typed["email"])
        if dono is not None:
            if self.__usuariosjuridicos[dono].cnpj == typed["cnpj"]:
                return dono
            else:
                return None

    def listar_usuario_fisico(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usario_fisico(typed["email"])
        if usuario is not None:
            self.__telaUsuario.mensagem_pro_usuario(self.__usuariosfisicos[usuario].nome)
            self.__telaUsuario.mensagem_pro_usuario(self.__usuariosfisicos[usuario].email)
            self.__telaUsuario.mensagem_pro_usuario(self.__usuariosfisicos[usuario].cpf)
        else:
            self.__telaUsuario.mensagem_pro_usuario("ATENCAO: Usuario não existente")

    def listar_usuario_juridico(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usuario_juridico(typed["email"])
        if usuario is not None:
            self.__telaUsuario.mensagem_pro_usuario(self.__usuariosjuridicos[usuario].nome)
            self.__telaUsuario.mensagem_pro_usuario(self.__usuariosjuridicos[usuario].email)
            self.__telaUsuario.mensagem_pro_usuario(self.__usuariosjuridicos[usuario].cnpj)
        else:
            self.__telaUsuario.mensagem_pro_usuario("ATENCAO: Usuario não existente")

    def retornar(self):
        self.__controladorSistema.abre_tela()

    def abretela(self):
        lista_opcoes = {1: self.realizaloginfisico, 2: self.realizaloginjuridico, 3: self.cadastrar_pessoa_fisica,
                        4: self.cadastrar_pessoa_juridica, 5: self.alterar_conta_fisica, 6: self.alterar_conta_juridica,
                        7: self.excluir_conta_fisica, 8: self.excluir_conta_juridica, 9: self.listar_usuario_fisico,
                        10: self.listar_usuario_juridico,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__telaUsuario.telaopcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
