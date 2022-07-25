from limite.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaCategoria(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def telaopcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
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

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Categorias ----------', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Incluir Categoria',"RD1", key='1')],
            [sg.Radio('Alterar Categorias',"RD1", key='2')],
            [sg.Radio('Excluir Categorias',"RD1", key='3')],
            [sg.Radio('Listar Categorias',"RD1", key='4')],
            [sg.Radio('Voltar Para Tela Inicial',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)

    def pega_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Cadastrar Categoria ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)

        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        if button in ('Confirmar'):
            try:
                nome = values['nome']
                descricao = values['descricao']
                if nome == '' or descricao == '' :
                    raise ValueError
                else:
                    self.close()
                    return {"nome": nome, "descricao": descricao}
            except ValueError:
                self.close()
                self.mensagem_pro_usuario('Valores não aceitos')
                return None

    def pega_nome(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        if button in ('Confirmar'):
            try:
                nome = values['nome']
                if nome == '':
                    raise ValueError
                else:
                    self.close()
                    return nome
            except ValueError:
                self.close()
                self.mensagem_pro_usuario('Valores não aceitos')
                return None

    def pega_descricao(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Nova Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return None
        if button in ('Confirmar'):
            try:
                descricao = values['descricao']
                if descricao == '':
                    raise ValueError
                else:
                    self.close()
                    return descricao
            except ValueError:
                self.close()
                self.mensagem_pro_usuario('Valores não aceitos')
                return None

    def lista_categoria(self, info_categoria):
        categorias = ""
        for dado in info_categoria:
            categorias = categorias + "NOME CATEGORIA: " + dado["nome"] + '\n'
            categorias = categorias + "DESCRICÂO: " + str(dado["descricao"]) + '\n\n'

        sg.Popup('-------- LISTA DE CATEGORIAS ----------', categorias)
    
    def mensagem_pro_usuario(self, msg):
        sg.Popup(msg)
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values