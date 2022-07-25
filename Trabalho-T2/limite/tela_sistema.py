from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaSistema(TelaAbstrata):
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
            [sg.Text('-------- Tela Usuarios ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Produtos', "RD1", key='1')],
            [sg.Radio("Usuarios", "RD1", key='2')],
            [sg.Radio("Supermercados", "RD1", key='3')],
            [sg.Radio("Categoria", "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
                  ]
        self.__window = sg.Window('Window Title').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
