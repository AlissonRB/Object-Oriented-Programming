from tkinter import Button
from limite.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaQualificador(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos= None):
        pass
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor numérico valido")
                if inteiros_validos:
                    print("Valores validos:", inteiros_validos)

    def pega_codigo(self, mensagem, codigos_validos):
        num_opcao = self.le_numero_inteiro(mensagem, codigos_validos)
        return num_opcao

    def pega_dados(self):
        sg.ChangeLookAndFeel('HotDogStand')
        layout = [
        [sg.Text('-------- Adicionar Qualificador ----------', font=("Helvica", 25))],
        [sg.Text('Titulo Qualificador:', size=(15, 1)), sg.InputText('', key='titulo_qualificador')],
        [sg.Text('Descricao Qualificador:', size=(15, 1)), sg.InputText('', key='descricao_qualificador')],
        [sg.Button(('Confirmar')), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        titulo_qualificador = values['titulo_qualificador']
        descricao_qualificador = values['descricao_qualificador']

        self.close()
        return {'titulo': titulo_qualificador, 'descricao': descricao_qualificador}
    
    def continuar(self):
        sg.ChangeLookAndFeel('HotDogStand')
        layout = [
        [sg.Text('-------- Adicionar mais qualificadores ? ----------', font=("Helvica", 25))],
        [sg.Radio('Sim',"RD1", key='1')],
        [sg.Radio('Não',"RD1", key='0')],
        [sg.Button(('Confirmar')), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def telaopcoes(self):
        pass

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values