class UsuarioJaCadastradoException(Exception):
    def __init__(self):
        self.mensagem = "Erro: Usuario Ja Cadastrado"
        super().__init__(self.mensagem.format())
