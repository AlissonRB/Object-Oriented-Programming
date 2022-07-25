from limite.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaProduto(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

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
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Produtos ----------', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Incluir Produto',"RD1", key='1')],
            [sg.Radio('Pesquisar Precos de Produtos',"RD1", key='2')],
            [sg.Radio('Lançar Preço',"RD1", key='3')],
            [sg.Radio('Excluir Produto',"RD1", key='4')],
            [sg.Radio('Registros de um Produto', "RD1", key='5')],
            [sg.Radio('Relatórios', "RD1", key='6')],
            [sg.Radio('Voltar Para Tela Inicial',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
    
    def pega_dados(self,categorias, supermercados):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Cadastrar Produto ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Descricao:', size=(15, 1)), sg.InputText('', key='descricao')],
        [sg.Text('preço:', size=(15, 1)), sg.InputText('', key='preco')],
        [sg.Text('Categoria:'),sg.InputCombo((categorias), size=(20, 3), key='categoria'),sg.Text('Supermercado:'),sg.InputCombo((supermercados), size=(20, 3),key='supermercado')],
        [sg.Button(('Confirmar')), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return None
        if button in ('Confirmar'):
            try:
                nome = values['nome']
                descricao = values['descricao']
                preco = float(values['preco'])
                categoria = values['categoria']
                mercado = values['supermercado']
                if nome and descricao and preco and categoria and mercado is not None:
                    self.close()
                    return {"nome": nome, "descricao": descricao, "preco": preco, 'categoria': categoria, 'mercado': mercado}
                else:
                    raise ValueError
            except ValueError:
                self.close()
                self.mensagem_pro_usuario('Valores não aceitos')
                return None

    def lancamento_preco(self,descricao_categoria, descricao_mercado):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Lançamento de Preços ----------', font=("Helvica", 25))],
        [sg.Text('Supermercado:'),sg.InputCombo(( descricao_mercado), size=(20, 3),key='supermercado'),sg.Text('Categoria:'),
        sg.InputCombo((descricao_categoria), size=(20, 3), key='categoria')],
        [sg.Text('Nome Produto:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Novo preço:', size=(15, 1)), sg.InputText('', key='preco')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        if button in ('Confirmar'):
            try:
                supermercado = values['supermercado']
                categoria = values['categoria']
                nome = values['nome']
                preco = float(values['preco'])
                if supermercado and categoria and preco and categoria and nome is not None:
                    self.close()
                    return {"nome": nome, "preco": preco, 'categoria': categoria, 'supermercado': supermercado}
                else:
                    raise ValueError
            except ValueError:
                self.close()
                self.mensagem_pro_usuario('Valores não aceitos')
                return None

    def pesquisar_preco(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Nome Produto:', size=(15, 1)), sg.InputText('', key='nome')],
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
                    return {"nome": nome}
            except ValueError:
                self.close()
                self.mensagem_pro_usuario('Valores não aceitos')
                return None

    def pega_nome(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Nome Mercado:'),sg.InputCombo((msg), size=(20, 3), key='nome')],
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

    def produtos_por_mercado(self, lista_produtos):
        string_produtos = ""
        for dado in lista_produtos:
            string_produtos = string_produtos + "Produto: " + dado["nome"] + '\n'
            string_produtos = string_produtos + "Preço: " + "{:.2f}".format(dado["preco"]) + '\n'
            string_produtos = string_produtos + "Categoria: " + str(dado["categoria"]) + '\n'
            string_produtos = string_produtos + "Codigo: " + str(dado["codigo"]) + '\n\n'


        sg.Popup('-------- PRODUTOS POR SUPERMERCADO ----------', string_produtos)
    
    def mostra_resultados_busca(self, dados_produto):
 
        string_dados = ""
        for dado in dados_produto:
            string_dados = string_dados + "NOME DO PRODUTO: " + dado["nome"] + '\n'
            string_dados = string_dados + "PREÇO: " + "{:.2f}".format(dado["preco"]) + '\n'
            string_dados = string_dados + "SUPERMERCADO: " + str(dado["mercado"]) + '\n\n'

        sg.Popup('-------- PESQUISA PREÇOS ----------', string_dados)

    def precos_produto(self, nome, info_precos):
        nome = nome
        precos = ""
        for dado in info_precos:
            precos = precos + "R$: {:.2f}".format(dado) + '\n'

        sg.Popup(f'-------- Precos de {nome}  ----------', precos)

    def mostra_registros(self, dados_registro):
        string_registros = ""
        for dado in dados_registro:
            string_registros = string_registros + "Data: " + str(dado["data"]) + '\n'
            string_registros = string_registros + "Operação: " + str(dado["operacao"]) + '\n'
            string_registros = string_registros + "valor: " + "R$: {:.2f}".format(dado["valor"]) + '\n'
            string_registros = string_registros + "Usuario: " + str(dado["usuario"]) + '\n\n'

        sg.Popup('-------- Registros de um Produto ----------', string_registros)

    def relatorios(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Relatórios ----------', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Produtos por Supermercado',"RD1", key='1')],
            [sg.Radio('Lista de Preços de um Produto',"RD1", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def pega_inteiro(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Codigo:'),sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        if button in ('Confirmar'):
            try:
                codigo = values['codigo']
                if codigo == '':
                    raise ValueError
                else:
                    self.close()
                    return codigo
            except ValueError:
                self.close()
                self.mensagem_pro_usuario('Valores não aceitos')
                return None

    def mensagem_pro_usuario(self, msg):
        sg.Popup(msg)
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values