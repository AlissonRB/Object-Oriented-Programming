class UsuarioNaoExistenteException(Exception):
    def __init__(self):
        self.mensagem = "ERRO: Usuario não existente"
        super().__init__(self.mensagem.format())
