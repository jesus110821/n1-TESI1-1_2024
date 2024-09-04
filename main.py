import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Sistema Bancário')
        self.janela.geometry('400x300')

        # Barra de menu
        self.mnu_barra = tk.Menu(self.janela)

        # Menus
        self.mnu_banco = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_conta = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_cliente = tk.Menu(self.mnu_barra, tearoff=0)

        # Adicionando os menus à barra de menu
        self.mnu_barra.add_cascade(label='Banco', menu=self.mnu_banco)
        self.mnu_barra.add_cascade(label='Conta', menu=self.mnu_conta)
        self.mnu_barra.add_cascade(label='Cliente', menu=self.mnu_cliente)

        # Adicionando comandos ao menu Banco
        self.mnu_banco.add_command(label='Cadastrar Banco', command=self.cadastrar_banco)
        self.mnu_banco.add_separator()

        # Adicionando comandos ao menu Conta
        self.mnu_conta.add_command(label='Cadastrar Conta Corrente', command=self.cadastrar_conta_corrente)
        self.mnu_conta.add_command(label='Cadastrar Conta Poupança', command=self.cadastrar_conta_poupanca)
        self.mnu_conta.add_separator()

        # Adicionando comandos ao menu Cliente
        self.mnu_cliente.add_command(label='Cadastrar Cliente', command=self.cadastrar_cliente)
        self.mnu_cliente.add_separator()

        # Configurando a barra de menu na janela
        self.janela.config(menu=self.mnu_barra)

    # Função para abrir a janela de cadastro de banco
    def cadastrar_banco(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Cadastrar Banco')
        nova_janela.geometry('300x200')
        lbl_banco = tk.Label(nova_janela, text='Cadastro de Banco')
        lbl_banco.pack(pady=10)

    # Função para abrir a janela de cadastro de conta corrente
    def cadastrar_conta_corrente(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Cadastrar Conta Corrente')
        nova_janela.geometry('300x200')
        lbl_conta_corrente = tk.Label(nova_janela, text='Cadastro de Conta Corrente')
        lbl_conta_corrente.pack(pady=10)

    # Função para abrir a janela de cadastro de conta poupança
    def cadastrar_conta_poupanca(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Cadastrar Conta Poupança')
        nova_janela.geometry('300x200')
        lbl_conta_poupanca = tk.Label(nova_janela, text='Cadastro de Conta Poupança')
        lbl_conta_poupanca.pack(pady=10)

    # Função para abrir a janela de cadastro de cliente
    def cadastrar_cliente(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Cadastrar Cliente')
        nova_janela.geometry('300x200')
        lbl_cliente = tk.Label(nova_janela, text='Cadastro de Cliente')
        lbl_cliente.pack(pady=10)

# Criação da janela principal
janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
