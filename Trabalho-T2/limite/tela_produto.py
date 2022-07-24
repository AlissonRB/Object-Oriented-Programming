from click import command
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
        if values['7']:
            opcao = 7
        if values['0'] or button in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel('HotDogStand')
        layout = [
            [sg.Text('-------- Produtos ----------', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Incluir Produto',"RD1", key='1')],
            [sg.Radio('Pesquisar Precos de Produtos',"RD1", key='2')],
            [sg.Radio('Lançar Preço',"RD1", key='3')],
            [sg.Radio('Excluir Produto',"RD1", key='4')],
            [sg.Radio('Registros de um Produto', "RD1", key='5')],
            [sg.Radio('Relatórios', "RD1", key='6')],
            [sg.Radio('Excluir Preço', "RD1", key='7')],
            [sg.Radio('Voltar Para Tela Inicial',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)

    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos = None):
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
                    print("Valores validos: ", inteiros_validos)
    
    def pega_dados(self,categorias, supermercados):
        sg.ChangeLookAndFeel('HotDogStand')
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
        
        nome = values['nome']
        descricao = values['descricao']
        preco = int(values['preco'])
        categoria = values['categoria']
        mercado = values['supermercado']

        self.close()
        return {"nome": nome, "descricao": descricao, "preco": preco, 'categoria': categoria, 'mercado': mercado}

    def lancamento_preco(self,descricao_categoria, descricao_mercado):
        sg.ChangeLookAndFeel('HotDogStand')
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

        supermercado = values['supermercado']
        categoria = values['categoria']
        nome = values['nome']
        preco = values['preco']

        self.close()

        return {"nome": nome, "preco": preco, 'categoria': categoria, 'supermercado': supermercado}

    def pesquisar_preco(self):
        sg.ChangeLookAndFeel('HotDogStand')
        layout = [
            [sg.Text('Nome Produto:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        nome = values['nome']
        self.close()

        return {"nome": nome}
        

    def pega_nome(self, msg):
        sg.ChangeLookAndFeel('HotDogStand')
        layout = [
            [sg.Text('Mercado:'),sg.InputCombo((msg), size=(20, 3), key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        nome = values['nome']
        self.close()

        return nome
    
    def pega_preço(self):
        while True:
            try:
                preco = float(input("Preço: " )) #converter para duas casas
                if not isinstance(preco,float):
                    raise ValueError
                return preco
            except ValueError:
                print("Valor inválido !")

    def produtos_por_mercado(self, lista_produtos):
        string_todos_amigos = ""
        for dado in lista_produtos:
            string_todos_amigos = string_todos_amigos + "Produto: " + dado["nome"] + '\n'
            string_todos_amigos = string_todos_amigos + "Preço: " + str(dado["preco"]) + '\n'
            string_todos_amigos = string_todos_amigos + "Categoria: " + str(dado["categoria"]) + '\n'
            string_todos_amigos = string_todos_amigos + "Codigo: " + str(dado["codigo"]) + '\n\n'


        sg.Popup('-------- PRODUTOS POR SUPERMERCADO ----------', string_todos_amigos)
    
    def mostra_resultados_busca(self, dados_produto):
 
        string_dados = ""
        for dado in dados_produto:
            string_dados = string_dados + "NOME DO PRODUTO: " + dado["nome"] + '\n'
            #string_dados = string_dados + "QUALIFICADOR: " + str(dado["qualificador"]) + '\n'
            string_dados = string_dados + "PREÇO: " + str(dado["preco"]) + '\n'
            string_dados = string_dados + "SUPERMERCADO: " + str(dado["mercado"]) + '\n\n'

        sg.Popup('-------- PESQUISA PREÇOS ----------', string_dados)

    def precos_produto(self, nome, info_precos):
        nome = nome
        precos = ""
        for dado in info_precos:
            precos = precos + "R$: " + str(dado) + '\n'

        sg.Popup(f'-------- Precos de {nome}  ----------', precos)

    def mostra_registros(self, dados_registro):
        #print(dados_registro["data"], dados_registro["operacao"], dados_registro["valor"])
        #print("\n")
        string_registros = ""
        for dado in dados_registro:
            string_registros = string_registros + "Data: " + str(dado["data"]) + '\n'
            string_registros = string_registros + "Operação: " + str(dado["operacao"]) + '\n'
            string_registros = string_registros + "valor: " + str(dado["valor"]) + '\n'
            string_registros = string_registros + "Usuario: " + str(dado["usuario"]) + '\n\n'

        sg.Popup('-------- Registros de um Produto ----------', string_registros)

    def relatorios(self):
        sg.ChangeLookAndFeel('HotDogStand')
        layout = [
            [sg.Text('-------- Relatórios ----------', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Produtos por Supermercado',"RD1", key='1')],
            [sg.Radio('Evolução dos Preços',"RD1", key='2')],
            [sg.Radio('Lista de Preços de um Produto',"RD1", key='3')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def pega_inteiro(self):#fazer o tratamento aqui , tentar conerter para string o codigo
        sg.ChangeLookAndFeel('HotDogStand')
        layout = [
            [sg.Text('Codigo:'),sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Supermercado').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        codigo = values['codigo']
        self.close()
        return codigo

        while True:
            try:
                codigo = int(input(msg))
                if not isinstance(codigo,int):
                    raise ValueError
                return codigo
            except ValueError:
                print("Valor inválido:")

    def pega_float(self, msg):
        while True:
            try:
                codigo = float(input(msg))
                if not isinstance(codigo,float):
                    raise ValueError
                return codigo
            except ValueError:
                print("Valor inválido:")

    def mensagem_pro_usuario(self, msg):
        sg.Popup(msg)
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
