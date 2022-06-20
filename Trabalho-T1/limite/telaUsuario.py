from limite.telaAbstrata import TelaAbstrata


class TelaUsuario(TelaAbstrata):
    def __init__(self):
        super().__init__()

    def tela_login_fisica(self):
        email = input("Email: ")
        cpf = input("Cpf: ")
        return {"email": email, "cpf": cpf}

    def tela_login_juridica(self):
        email = input("Email: ")
        cnpj = input("Cnpj: ")
        return {"email": email, "cnpj": cnpj}

    def le_numero_inteiro(self, mensagem, inteiros_validos):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor Incorreto, Digite um Valor Valido")
                if inteiros_validos:
                    print("Valores Validos: ", inteiros_validos)

    def telaopcoes(self):
        print("------Tela Usuarios------")
        print("1 - Fazer Login Pessoa Fisica")
        print("2 - Fazer Login Pessoa Juridica")
        print("3 - Fazer Cadastro Pessoa Fisica")
        print("4 - Fazer Cadastro Pessoa Juridica")
        print("5 - Alterar Dados Pessoa Fisica")
        print("6 - Alterar Dados Pessoa Juridica")
        print("7 - Excluir Conta Fisica")
        print("8 - Excluir Conta Juridica")
        print("9 - Listar Conta Fisica")
        print("10 - Listar Conta Juridica")
        print("0 - Voltar")
        opcao = self.le_numero_inteiro("Escolha sua opcao: ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
        return opcao

    def tela_inicial(self):
        pass

    def pega_dados_conta_juridica(self):
        print("-----Digite os Dados-----")
        nome = input("Nome :")
        email = input("Email: ")
        cnpj = input("Cnpj: ")
        return {"nome": nome, "email": email, "cnpj": cnpj}

    def pega_dados_conta_fisica(self):
        print("-----Digite os Dados-----")
        nome = input("Nome :")
        email = input("Email: ")
        cpf = input("Cpf: ")
        return {"nome": nome, "email": email, "cpf": cpf}

    def mostra_dados_conta(self):
        pass

    def mensagem_pro_usuario(self, mensagem: str):
        print(mensagem)

    def seleciona_usuario(self):
        email = input("Email do Usario que deseja selecionar: ")
        return {"email": email}
