from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaUsuario(TelaAbstrata):
    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_opcoes_tela_inicial()

    def tela_login_fisica(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- LOGIN ----------', font=("Helvica", 25))],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Login Pessoa Fisica').Layout(layout)

        button, values = self.open()
        email = values['email']
        cpf = values['cpf']
        self.close()
        if button == "Voltar":
            self.tela_inicial_opcoes()
        else:
            return {"email": email, "cpf": cpf}

    def tela_login_juridica(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- LOGIN ----------', font=("Helvica", 25))],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Login Pessoa Juridica').Layout(layout)

        button, values = self.open()
        email = values['email']
        cnpj = values['cnpj']

        self.close()
        if button == "Voltar":
            self.tela_inicial_opcoes()
        else:
            return {"email": email, "cnpj": cnpj}

    def init_tela_opcoes(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- Tela Usuarios ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Fazer Cadastro Pessoa Fisica', "RD1", key='1')],
            [sg.Radio("Fazer Cadastro Pessoa Juridica", "RD1", key='2')],
            [sg.Radio("Alterar Dados Pessoa Fisica", "RD1", key='3')],
            [sg.Radio("Alterar Dados Pessoa Juridica", "RD1", key='4')],
            [sg.Radio("Excluir Conta Fisica", "RD1", key='5')],
            [sg.Radio("Excluir Conta Juridica", "RD1", key='6')],
            [sg.Radio("Listar Conta Fisica", "RD1", key='7')],
            [sg.Radio("Listar Conta Juridica", "RD1", key='8')],
            [sg.Radio("Deslogar", "RD1", key='9')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
                  ]
        self.__window = sg.Window('Window Title').Layout(layout)

    def init_opcoes_tela_inicial(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- Tela Inicial ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Login Fisico', "RD1", key='1')],
            [sg.Radio("Login Juridico", "RD1", key='2')],
            [sg.Radio("Cadastro Fisico", "RD1", key='3')],
            [sg.Radio("Cadastro Juridico", "RD1", key='4')],
            [sg.Radio('Fechar Programa', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                  ]
        self.__window = sg.Window('Window Title').Layout(layout)

    def tela_inicial_opcoes(self):
        self.init_opcoes_tela_inicial()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def telaopcoes(self):
        self.init_tela_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['9']:
            opcao = 9
        if button in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def pega_dados_conta_juridica(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS Usuario ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Cadastro Pessoa Juridico').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        email = values['email']
        cnpj = values['cnpj']

        self.close()
        if button == "Voltar":
            self.tela_inicial_opcoes()
        elif button == "Confirmar":
            return {"nome": nome, "email": email, "cnpj": cnpj}

    def pega_dados_conta_fisica(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS Usuario ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Cadastro Pessoa Fisica').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        email = values['email']
        cpf = values['cpf']

        self.close()
        if button == "Voltar":
            self.tela_inicial_opcoes()
        elif button == "Confirmar":
            return {"nome": nome, "email": email, "cpf": cpf}

    def mensagem_pro_usuario(self, mensagem: str):
        sg.popup("", mensagem)

    def seleciona_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR Usuario ----------', font=("Helvica", 25))],
            [sg.Text('Digite o Email do usuario que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Seleciona Usuario').Layout(layout)

        button, values = self.open()
        email = values['email']
        self.close()
        return {"email": email}

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
