from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaSupermercado(TelaAbstrata):
    def __init__(self):
        super().__init__()

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
        if button in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def init_tela_opcoes(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- Tela Supermercado ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Mercado', "RD1", key='1')],
            [sg.Radio("Alterar Mercado", "RD1", key='2')],
            [sg.Radio("Excluir Mercado", "RD1", key='3')],
            [sg.Radio("Listar Mercados", "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Window Title').Layout(layout)

    def pega_dados_supermercado(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Digite os Dados Do Mercado ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Endereco:', size=(15, 1)), sg.InputText('', key='endereco')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Supermercado').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        endereco = values['endereco']
        self.close()
        if button == "Voltar":
            self.tela_inicial_opcoes()
        else:
            return {"nome": nome, "endereco": endereco}


    def mensagem_pro_usuario(self, mensagem: str):
        sg.popup("", mensagem)

    def seleciona_mercado(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR Mercado ----------', font=("Helvica", 25))],
            [sg.Text('Digite o Nome do Mercado que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Seleciona Supermercado').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return {"nome": nome}

    def dados_dono(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Seleciona Dono ----------', font=("Helvica", 25))],
            [sg.Text('Digite o CNPJ do Mercado:', font=("Helvica", 15))],
            [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Seleciona Supermercado').Layout(layout)

        button, values = self.open()
        cnpj = values['cnpj']
        self.close()
        return {"cnpj": cnpj}

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
