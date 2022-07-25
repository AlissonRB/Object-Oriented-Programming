from limite.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaQualificador(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def pega_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Adicionar Qualificador ----------', font=("Helvica", 25))],
        [sg.Text('Titulo Qualificador:', size=(15, 1)), sg.InputText('', key='titulo_qualificador')],
        [sg.Text('Descricao Qualificador:', size=(15, 1)), sg.InputText('', key='descricao_qualificador')],
        [sg.Button(('Confirmar')), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        if button in ('Confirmar'):
            try:
                titulo_qualificador = values['titulo_qualificador']
                descricao_qualificador = values['descricao_qualificador']
                if titulo_qualificador or descricao_qualificador == '':
                    raise ValueError
                else:
                    self.close()
                    return {'titulo': titulo_qualificador, 'descricao': descricao_qualificador}
            except ValueError:
                self.close()
                self.mensagem_pro_usuario('Nenhum Qualificador Adicionado')
                return None
    
    def continuar(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Adicionar mais qualificadores ? ----------', font=("Helvica", 25))],
        [sg.Radio('Sim',"RD1", key='1')],
        [sg.Radio('Não',"RD1", key='0')],
        [sg.Button(('Confirmar')), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
            self.close()
            return opcao
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
            self.close()
            return opcao

    def telaopcoes(self):
        pass

    def mensagem_pro_usuario(self, msg):
        sg.Popup(msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values