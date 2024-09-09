import tkinter as tk
from tkinter import messagebox

class Banco:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome

class SistemaBancario:
    def __init__(self):
        self.bancos = []

    def cadastrar_bancos(self, numero, nome):
        novo_banco = Banco(numero,nome)
        self.bancos.append(novo_banco)

    def listar_bancos(self):
        return self.bancos

    def atualizar_banco(self, banco, novo_nome):
        banco.nome = novo_nome


sistema = SistemaBancario()

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Sistema Bancário')
        self.janela.geometry('400x300')

        self.mnu_barra = tk.Menu(self.janela)

        self.mnu_banco = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_conta = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_cliente = tk.Menu(self.mnu_barra, tearoff=0)

        self.mnu_barra.add_cascade(label='Banco', menu=self.mnu_banco)
        self.mnu_barra.add_cascade(label='Conta', menu=self.mnu_conta)
        self.mnu_barra.add_cascade(label='Cliente', menu=self.mnu_cliente)

        self.mnu_banco.add_command(label='Cadastrar Banco', command=self.cadastrar_banco)
        self.mnu_banco.add_command(label='Mostrar Banco', command=self.mostrar_banco)
        # self.mnu_banco.add_command(label='Atualizar Banco', command=self.atualizar_banco)
        self.mnu_banco.add_separator()

        self.mnu_conta.add_command(label='Cadastrar Conta Corrente', command=self.cadastrar_conta_corrente)
        self.mnu_conta.add_command(label='Cadastrar Conta Poupança', command=self.cadastrar_conta_poupanca)
        self.mnu_conta.add_separator()

        self.mnu_cliente.add_command(label='Cadastrar Cliente', command=self.cadastrar_cliente)
        self.mnu_cliente.add_command(label='Mostrar CLiente', command=self.mostrar_cliente)
        self.mnu_cliente.add_separator()

        self.janela.config(menu=self.mnu_barra)

    def cadastrar_banco(self):
        self.nova_janela = tk.Toplevel(self.janela)
        self.nova_janela.title('Cadastrar Banco')
        self.nova_janela.geometry('300x200')

        lbl_numero = tk.Label(self.nova_janela, text='Número do Banco:')
        lbl_numero.pack(pady=5)
        self.ent_numero = tk.Entry(self.nova_janela)
        self.ent_numero.pack(pady=5)

        lbl_nome = tk.Label(self.nova_janela, text='Nome do Banco:')
        lbl_nome.pack(pady=5)
        self.ent_nome = tk.Entry(self.nova_janela)
        self.ent_nome.pack(pady=5)

        btn_salvar = tk.Button(self.nova_janela, text='Salvar', command=self.salvar_banco)
        btn_salvar.pack(pady=10)

    def salvar_banco(self):
        numero = self.ent_numero.get()
        nome = self.ent_nome.get()
        if numero and nome:
            sistema.cadastrar_bancos(numero, nome)
            messagebox.showinfo('Sucesso','Banco cadastrado com sucesso!')
            self.nova_janela.destroy()
        else:
            messagebox.showwarning('Atenção','Preencha todos os campos!')


    def mostrar_banco(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Mostrar Banco')
        nova_janela.geometry('300x200')
        lbl_banco = tk.Label(nova_janela, text='Bancos Cadastrados')
        lbl_banco.pack(pady=10)

    def cadastrar_conta_corrente(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Cadastrar Conta Corrente')
        nova_janela.geometry('300x200')
        lbl_conta_corrente = tk.Label(nova_janela, text='Cadastro de Conta Corrente')
        lbl_conta_corrente.pack(pady=10)

    def cadastrar_conta_poupanca(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Cadastrar Conta Poupança')
        nova_janela.geometry('300x200')
        lbl_conta_poupanca = tk.Label(nova_janela, text='Cadastro de Conta Poupança')
        lbl_conta_poupanca.pack(pady=10)

    def cadastrar_cliente(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Cadastrar Cliente')
        nova_janela.geometry('300x200')
        lbl_cliente = tk.Label(nova_janela, text='Cadastro de Cliente')
        lbl_cliente.pack(pady=10)

    def mostrar_cliente(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Mostrar Cliente')
        nova_janela.geometry('300x200')
        lbl_cliente = tk.Label(nova_janela,text='Clientes Cadastrados')
        lbl_cliente.pack(pady=10)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
