from limite.tela_usuario import TelaUsuario
from entidade.usuarioFisico import UsuarioFisico
from entidade.usuarioJuridico import UsuarioJuridico
from controle.usuario_ja_cadastrado_exception import UsuarioJaCadastradoException
from controle.usuario_nao_existente_exception import UsuarioNaoExistenteException
from DAOs.usuario_fisico_dao import UsuarioFisicoDao
from DAOs.usuario_juridico_dao import UsuarioJuridicoDao


class ControladorUsuario:

    def __init__(self, controlador_sistema):
        self.__usuario_juridico_Dao = UsuarioJuridicoDao()
        self.__usuario_fisico_Dao = UsuarioFisicoDao()
        self.__telaUsuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def pega_usuario_juridico(self, email: str):
        for usuario_juridico in self.__usuario_juridico_Dao.get_all():
            if usuario_juridico.email == email:
                return usuario_juridico
        return None

    def pega_usario_fisico(self, email: str):
        for usuario_fisico in self.__usuario_fisico_Dao.get_all():
            if usuario_fisico.email == email:
                return usuario_fisico
        return None

    def retorna_usuario_fisico(self, email: str):
        for usuario_fisico in self.__usuario_fisico_Dao.get_all():
            if usuario_fisico.email == email:
                return usuario_fisico
        return None

    def retorna_usuario_juridico(self, email: str):
        for usuario_juridico in self.__usuario_juridico_Dao.get_all():
            if usuario_juridico.email == email:
                return usuario_juridico
        return None

    def realizaloginfisico(self):
        typed = self.__telaUsuario.tela_login_fisica()
        if typed is None:
            pass
        else:
            verifica_usuario = self.pega_usario_fisico(typed["email"])
            if verifica_usuario is not None:
                if verifica_usuario.cpf == typed["cpf"]:
                    self.__telaUsuario.mensagem_pro_usuario("Seja bem vindo!")
                    self.__controlador_sistema.usuario_logado = verifica_usuario
                    self.__controlador_sistema.abre_tela()
                else:
                    self.__telaUsuario.mensagem_pro_usuario("Informações de login incorretas!")
            else:
                self.__telaUsuario.mensagem_pro_usuario("Informações de login incorretas!")

    def realizaloginjuridico(self):
        typed = self.__telaUsuario.tela_login_juridica()
        if typed is None:
            pass
        else:
            verifica_usuario = self.pega_usuario_juridico(typed["email"])
            if verifica_usuario is not None:
                if verifica_usuario.cnpj == typed["cnpj"]:
                    self.__telaUsuario.mensagem_pro_usuario("Seja bem vindo!")
                    self.__controlador_sistema.usuario_logado = verifica_usuario
                    self.__controlador_sistema.abre_tela()
                else:
                    self.__telaUsuario.mensagem_pro_usuario("Informações de login incorretas!")
            else:
                self.__telaUsuario.mensagem_pro_usuario("Informações de login incorretas!")

    def cadastrar_pessoa_juridica(self):
        typed = self.__telaUsuario.pega_dados_conta_juridica()
        if typed is None:
            pass
        else:
            try:
                pessoa_juridica = UsuarioJuridico(typed["nome"], typed["email"], typed["cnpj"])
                verifica_usuario = self.pega_usuario_juridico(typed["email"])
                if verifica_usuario == None:
                    self.__usuario_juridico_Dao.add(pessoa_juridica)
                    self.__telaUsuario.mensagem_pro_usuario("Cadastrado Com Sucesso")
                    self.__controlador_sistema.usuario_logado = pessoa_juridica
                    self.__controlador_sistema.abre_tela()

                else:
                    raise (UsuarioJaCadastradoException())
            except UsuarioJaCadastradoException as e:
                self.__telaUsuario.mensagem_pro_usuario(e)

    def cadastrar_pessoa_fisica(self):
        typed = self.__telaUsuario.pega_dados_conta_fisica()
        if typed is None:
            pass
        else:
            try:
                pessoa_fisica = UsuarioFisico(typed["nome"], typed["email"], typed["cpf"])
                verifica_usuario = self.pega_usuario_juridico(typed["email"])
                if verifica_usuario == None:
                    self.__usuario_fisico_Dao.add(pessoa_fisica)
                    self.__telaUsuario.mensagem_pro_usuario("Cadastrado Com Sucesso")
                    self.__controlador_sistema.usuario_logado = pessoa_fisica
                    self.__controlador_sistema.abre_tela()
                else:
                    raise (UsuarioJaCadastradoException())
            except UsuarioJaCadastradoException as e:
                self.__telaUsuario.mensagem_pro_usuario(e)

    def alterar_conta_fisica(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usario_fisico(typed["email"])
        try:
            if usuario is not None:
                novos_dados_usuario = self.__telaUsuario.pega_dados_conta_fisica()
                self.__usuario_fisico_Dao.remove(usuario.email)
                pessoa_fisica = UsuarioFisico(novos_dados_usuario["nome"], novos_dados_usuario["email"],
                                              novos_dados_usuario["cpf"])
                verifica_usuario = self.__usuario_fisico_Dao.get(typed['email'])
                if verifica_usuario == None:
                    self.__usuario_fisico_Dao.add(pessoa_fisica)
                    self.__telaUsuario.mensagem_pro_usuario("Dados Alterados Com Sucesso")
                else:
                    self.__telaUsuario.mensagem_pro_usuario("Erro,Ja existe um usario com esses dados")
            else:
                raise (UsuarioNaoExistenteException())
        except UsuarioNaoExistenteException as e:
            self.__telaUsuario.mensagem_pro_usuario(e)

    def alterar_conta_juridica(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usuario_juridico(typed["email"])
        try:
            if usuario is not None:
                novos_dados_usuario = self.__telaUsuario.pega_dados_conta_juridica()
                self.__usuario_juridico_Dao.remove(usuario.email)
                pessoa_juridica = UsuarioJuridico(novos_dados_usuario["nome"], novos_dados_usuario["email"],
                                                  novos_dados_usuario["cnpj"])
                verifica_usuario = self.__usuario_fisico_Dao.get(typed['email'])
                if verifica_usuario == None:
                    self.__usuario_juridico_Dao.add(pessoa_juridica)
                    self.__telaUsuario.mensagem_pro_usuario("Dados Alterados Com Sucesso")
                else:
                    self.__telaUsuario.mensagem_pro_usuario("Erro,Ja existe um usario com esses dados")
            else:
                raise (UsuarioNaoExistenteException())
        except UsuarioNaoExistenteException as e:
            self.__telaUsuario.mensagem_pro_usuario(e)

    def excluir_conta_fisica(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usario_fisico(typed["email"])
        try:
            if usuario is not None:
                self.__usuario_fisico_Dao.remove(usuario.email)
                self.__telaUsuario.mensagem_pro_usuario("Usuario Removido com Sucesso")
            else:
                raise (UsuarioNaoExistenteException())
        except UsuarioNaoExistenteException as e:
            self.__telaUsuario.mensagem_pro_usuario(e)

    def excluir_conta_juridica(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usuario_juridico(typed["email"])
        try:
            if usuario is not None:
                self.__usuario_juridico_Dao.remove(usuario.email)
                self.__telaUsuario.mensagem_pro_usuario("Usuario Removido com Sucesso")
            else:
                raise (UsuarioNaoExistenteException())
        except UsuarioNaoExistenteException as e:
            self.__telaUsuario.mensagem_pro_usuario(e)

    def verifica_usuario_juridico(self):
        typed = self.__telaUsuario.tela_login_juridica()
        dono = self.pega_usuario_juridico(typed["email"])
        if dono is not None:
            if dono.cnpj == typed["cnpj"]:
                return dono
            else:
                return None

    def listar_usuario_fisico(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usario_fisico(typed["email"])
        try:
            if usuario is not None:
                self.__telaUsuario.mensagem_pro_usuario(f"{usuario.nome} "
                                                        f"{usuario.email}"
                                                        f" {usuario.cpf}")
            else:
                raise (UsuarioNaoExistenteException())
        except UsuarioNaoExistenteException as e:
            self.__telaUsuario.mensagem_pro_usuario(e)

    def listar_usuario_juridico(self):
        typed = self.__telaUsuario.seleciona_usuario()
        usuario = self.pega_usuario_juridico(typed["email"])
        try:
            if usuario is not None:
                self.__telaUsuario.mensagem_pro_usuario(f"{usuario.nome} "
                                                        f"{usuario.email}"
                                                        f" {usuario.cnpj}")
            else:
                raise (UsuarioNaoExistenteException())
        except UsuarioNaoExistenteException as e:
            self.__telaUsuario.mensagem_pro_usuario(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def deslogar(self):
        self.__controlador_sistema.usuario_logado = None
        self.abretela_inicial()

    def abretela(self):
        lista_opcoes = {1: self.cadastrar_pessoa_fisica,
                        2: self.cadastrar_pessoa_juridica, 3: self.alterar_conta_fisica, 4: self.alterar_conta_juridica,
                        5: self.excluir_conta_fisica, 6: self.excluir_conta_juridica, 7: self.listar_usuario_fisico,
                        8: self.listar_usuario_juridico, 9: self.deslogar, 0: self.retornar}

        while True:
            opcao_escolhida = self.__telaUsuario.telaopcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abretela_inicial(self):
        lista_opcoes = {1: self.realizaloginfisico, 2: self.realizaloginjuridico, 3: self.cadastrar_pessoa_fisica,
                        4: self.cadastrar_pessoa_juridica, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__telaUsuario.tela_inicial_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
