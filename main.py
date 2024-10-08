import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Conta import Conta, ContaPoupanca, ContaCorrente


class Banco:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome

class SistemaBancario:
    def __init__(self):
        self.bancos = []
        self.contas = []
        self.clientes = []

    def cadastrar_cliente(self, nome, cpf):
        novo_cliente = {'nome': nome, 'cpf': cpf}
        self.clientes.append(novo_cliente)

    def listar_clientes(self):
        return self.clientes

    def atualizar_cliente(self, cliente, novo_nome, novo_cpf):
        cliente['nome'] = novo_nome
        cliente['cpf'] = novo_cpf

    def cadastrar_bancos(self, numero, nome):
        novo_banco = Banco(numero, nome)
        self.bancos.append(novo_banco)

    def listar_bancos(self):
        return self.bancos

    def atualizar_banco(self, banco, novo_numero, novo_nome):
        banco.numero = novo_numero
        banco.nome = novo_nome

    def cadastrar_conta_corrente(self, numero, titular, saldo=0.0):
        nova_conta = Conta(numero, titular, saldo)
        self.contas.append(nova_conta)

    def cadastrar_conta_poupanca(self, numero, titular, saldo=0.0):
        nova_conta = ContaPoupanca(numero, titular, saldo)
        self.contas.append(nova_conta)

    def atualizar_saldo_poupanca(self):
        for conta in self.contas:
            if isinstance(conta, ContaPoupanca):
                conta.atualizar_saldo()

    def listar_contas(self):
        return self.contas

    def atualizar_conta(self, conta, novo_numero, novo_titular, novo_saldo):
        conta.numero = novo_numero
        conta.titular = novo_titular
        conta.saldo = novo_saldo

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
        self.mnu_banco.add_command(label='Atualizar Banco', command=self.selecionar_banco_para_atualizar)
        self.mnu_banco.add_separator()

        self.mnu_conta.add_command(label='Cadastrar Conta Corrente', command=self.cadastrar_conta_corrente)
        self.mnu_conta.add_command(label='Cadastrar Conta Poupança', command=self.cadastrar_conta_poupanca)
        self.mnu_conta.add_command(label='Mostrar Conta', command=self.mostrar_conta)
        self.mnu_conta.add_command(label='Atualizar Conta', command=self.selecionar_conta_para_atualizar)
        self.mnu_conta.add_command(label='Depositar', command=self.selecionar_conta_para_deposito)
        self.mnu_conta.add_command(label='Sacar', command=self.selecionar_conta_para_saque)
        self.mnu_conta.add_command(label='Histórico de Transações', command=self.mostrar_historico)
        self.mnu_conta.add_separator()

        self.mnu_cliente.add_command(label='Cadastrar Cliente', command=self.cadastrar_cliente)
        self.mnu_cliente.add_command(label='Mostrar Cliente', command=self.mostrar_cliente)
        self.mnu_cliente.add_command(label='Atualizar Cliente', command=self.selecionar_cliente_para_atualizar)

        self.mnu_cliente.add_separator()

        self.janela.config(menu=self.mnu_barra)


    def mostrar_historico(self):
        self.nova_janela_historico = tk.Toplevel(self.janela)
        self.nova_janela_historico.title('Histórico de Transações')
        self.nova_janela_historico.geometry('400x300')

        lbl_numero = tk.Label(self.nova_janela_historico, text='Número da Conta:')
        lbl_numero.pack(pady=5)
        self.ent_numero_conta_historico = tk.Entry(self.nova_janela_historico)
        self.ent_numero_conta_historico.pack(pady=5)

        btn_exibir_historico = tk.Button(self.nova_janela_historico, text='Mostrar Histórico', command=self.exibir_historico)
        btn_exibir_historico.pack(pady=10)

    def exibir_historico(self):
        numero_conta = self.ent_numero_conta_historico.get()

        for conta in sistema.contas:
            if conta.numero == numero_conta:
                historico = conta.mostrar_historico()
                if historico:
                    messagebox.showinfo('Histórico de Transações', historico)
                else:
                    messagebox.showinfo('Histórico de Transações', 'Nenhuma transação encontrada.')
                return

        messagebox.showwarning('Erro', 'Conta não encontrada!')

    def selecionar_conta_para_deposito(self):
        self.nova_janela_deposito = tk.Toplevel(self.janela)
        self.nova_janela_deposito.title('Depósito')
        self.nova_janela_deposito.geometry('300x200')

        lbl_numero = tk.Label(self.nova_janela_deposito, text='Número da Conta:')
        lbl_numero.pack(pady=5)
        self.ent_numero_conta = tk.Entry(self.nova_janela_deposito)
        self.ent_numero_conta.pack(pady=5)

        lbl_valor = tk.Label(self.nova_janela_deposito, text='Valor do Depósito:')
        lbl_valor.pack(pady=5)
        self.ent_valor_deposito = tk.Entry(self.nova_janela_deposito)
        self.ent_valor_deposito.pack(pady=5)

        btn_depositar = tk.Button(self.nova_janela_deposito, text='Depositar', command=self.depositar_valor)
        btn_depositar.pack(pady=10)

    def depositar_valor(self):
        numero_conta = self.ent_numero_conta.get()
        valor = float(self.ent_valor_deposito.get())

        for conta in sistema.contas:
            if conta.numero == numero_conta:
                if conta.depositar(valor):
                    messagebox.showinfo('Sucesso', f'Depósito de R${valor:.2f} realizado com sucesso!')
                else:
                    messagebox.showwarning('Erro', 'Valor inválido para depósito!')
                return

        messagebox.showwarning('Erro', 'Conta não encontrada!')

    def selecionar_conta_para_saque(self):
        self.nova_janela_saque = tk.Toplevel(self.janela)
        self.nova_janela_saque.title('Saque')
        self.nova_janela_saque.geometry('300x200')

        lbl_numero = tk.Label(self.nova_janela_saque, text='Número da Conta:')
        lbl_numero.pack(pady=5)
        self.ent_numero_conta_saque = tk.Entry(self.nova_janela_saque)
        self.ent_numero_conta_saque.pack(pady=5)

        lbl_valor = tk.Label(self.nova_janela_saque, text='Valor do Saque:')
        lbl_valor.pack(pady=5)
        self.ent_valor_saque = tk.Entry(self.nova_janela_saque)
        self.ent_valor_saque.pack(pady=5)

        btn_sacar = tk.Button(self.nova_janela_saque, text='Sacar', command=self.sacar_valor)
        btn_sacar.pack(pady=10)

    def sacar_valor(self):
        numero_conta = self.ent_numero_conta_saque.get()
        valor = float(self.ent_valor_saque.get())

        for conta in sistema.contas:
            if conta.numero == numero_conta:
                if conta.sacar(valor):
                    messagebox.showinfo('Sucesso', f'Saque de R${valor:.2f} realizado com sucesso!')
                else:
                    messagebox.showwarning('Erro', 'Saldo insuficiente ou valor inválido!')
                return

        messagebox.showwarning('Erro', 'Conta não encontrada!')

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


    def salvar_conta_poupanca(self):
        numero = self.ent_numero_conta.get()
        titular = self.ent_titular.get()
        if numero and titular:
            sistema.cadastrar_conta_poupanca(numero, titular)
            messagebox.showinfo('Sucesso', 'Conta Poupança cadastrada com sucesso!')
            self.nova_janela.destroy()
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

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

        listbox = tk.Listbox(nova_janela)
        listbox.pack(fill=tk.BOTH, expand=True)

        bancos = sistema.listar_bancos()
        if bancos:
            for banco in bancos:
                listbox.insert(tk.END, f"Número: {banco.numero}, Nome: {banco.nome}")
        else:
            listbox.insert(tk.END, "Nenhum banco cadastrado.")

    def selecionar_banco_para_atualizar(self):
        self.nova_janela_selecao = tk.Toplevel(self.janela)
        self.nova_janela_selecao.title('Selecionar Banco para Atualizar')
        self.nova_janela_selecao.geometry('300x300')

        lbl_selecao = tk.Label(self.nova_janela_selecao, text='Selecione o Banco:')
        lbl_selecao.pack(pady=10)

        self.listbox_bancos = tk.Listbox(self.nova_janela_selecao)
        self.listbox_bancos.pack(fill=tk.BOTH, expand=True)

        bancos = sistema.listar_bancos()
        if bancos:
            for banco in bancos:
                self.listbox_bancos.insert(tk.END, f"Número: {banco.numero}, Nome: {banco.nome}")
        else:
            self.listbox_bancos.insert(tk.END, "Nenhum banco cadastrado.")

        btn_atualizar = tk.Button(self.nova_janela_selecao, text='Atualizar', command=self.atualizar_banco)
        btn_atualizar.pack(pady=10)

    def atualizar_banco(self):
        selecao = self.listbox_bancos.curselection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione um banco para atualizar!")
            return

        index = selecao[0]
        banco_selecionado = sistema.listar_bancos()[index]

        self.nova_janela_atualizar = tk.Toplevel(self.janela)
        self.nova_janela_atualizar.title('Atualizar Banco')
        self.nova_janela_atualizar.geometry('300x200')

        lbl_numero = tk.Label(self.nova_janela_atualizar, text='Novo Número do Banco:')
        lbl_numero.pack(pady=5)
        self.ent_novo_numero = tk.Entry(self.nova_janela_atualizar)
        self.ent_novo_numero.pack(pady=5)
        self.ent_novo_numero.insert(0, banco_selecionado.numero)

        lbl_nome = tk.Label(self.nova_janela_atualizar, text='Novo Nome do Banco:')
        lbl_nome.pack(pady=5)
        self.ent_novo_nome = tk.Entry(self.nova_janela_atualizar)
        self.ent_novo_nome.pack(pady=5)
        self.ent_novo_nome.insert(0, banco_selecionado.nome)

        btn_salvar = tk.Button(self.nova_janela_atualizar, text='Salvar', command=lambda: self.salvar_atualizacao_banco(banco_selecionado))
        btn_salvar.pack(pady=10)

    def salvar_atualizacao_banco(self, banco_selecionado):
        novo_numero = self.ent_novo_numero.get()
        novo_nome = self.ent_novo_nome.get()
        if novo_numero and novo_nome:
            sistema.atualizar_banco(banco_selecionado, novo_numero, novo_nome)
            messagebox.showinfo('Sucesso', 'Banco atualizado com sucesso!')
            self.nova_janela_atualizar.destroy()
            self.nova_janela_selecao.destroy()
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

    def cadastrar_conta_corrente(self):
        self.nova_janela = tk.Toplevel(self.janela)
        self.nova_janela.title('Cadastrar Conta Corrente')
        self.nova_janela.geometry('300x200')

        lbl_numero = tk.Label(self.nova_janela, text='Número da Conta:')
        lbl_numero.pack(pady=5)
        self.ent_numero_conta = tk.Entry(self.nova_janela)
        self.ent_numero_conta.pack(pady=5)

        lbl_titular = tk.Label(self.nova_janela, text='Titular da Conta:')
        lbl_titular.pack(pady=5)
        self.ent_titular = tk.Entry(self.nova_janela)
        self.ent_titular.pack(pady=5)

        btn_salvar = tk.Button(self.nova_janela, text='Salvar', command=self.salvar_conta)
        btn_salvar.pack(pady=10)

    def salvar_conta(self):
        numero = self.ent_numero_conta.get()
        titular = self.ent_titular.get()
        if numero and titular:
            sistema.cadastrar_conta_corrente(numero, titular)
            messagebox.showinfo('Sucesso', 'Conta Corrente cadastrada com sucesso!')
            self.nova_janela.destroy()
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

    def mostrar_conta(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Mostrar Contas')
        nova_janela.geometry('300x200')

        lbl_contas = tk.Label(nova_janela, text='Contas Cadastradas')
        lbl_contas.pack(pady=10)

        listbox = tk.Listbox(nova_janela)
        listbox.pack(fill=tk.BOTH, expand=True)

        contas = sistema.listar_contas()
        if contas:
            for conta in contas:
                tipo_conta = "Poupança" if isinstance(conta, ContaPoupanca) else "Corrente"
                listbox.insert(tk.END,
                               f"{tipo_conta} - Número: {conta.numero}, Titular: {conta.titular}, Saldo: {conta.saldo}")
        else:
            listbox.insert(tk.END, "Nenhuma conta cadastrada.")

    def selecionar_conta_para_atualizar(self):
        self.nova_janela_selecao = tk.Toplevel(self.janela)
        self.nova_janela_selecao.title('Selecionar Conta para Atualizar')
        self.nova_janela_selecao.geometry('300x300')

        lbl_selecao = tk.Label(self.nova_janela_selecao, text='Selecione a Conta:')
        lbl_selecao.pack(pady=10)

        self.listbox_contas = tk.Listbox(self.nova_janela_selecao)
        self.listbox_contas.pack(fill=tk.BOTH, expand=True)

        contas = sistema.listar_contas()
        if contas:
            for conta in contas:
                self.listbox_contas.insert(tk.END,
                                           f"Número: {conta.numero}, Titular: {conta.titular}, Saldo: {conta.saldo}")
        else:
            self.listbox_contas.insert(tk.END, "Nenhuma conta cadastrada.")

        btn_atualizar = tk.Button(self.nova_janela_selecao, text='Atualizar', command=self.atualizar_conta)
        btn_atualizar.pack(pady=10)

    def atualizar_conta(self):
        selecao = self.listbox_contas.curselection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma conta para atualizar!")
            return

        index = selecao[0]
        conta_selecionada = sistema.listar_contas()[index]

        self.nova_janela_atualizar = tk.Toplevel(self.janela)
        self.nova_janela_atualizar.title('Atualizar Conta')
        self.nova_janela_atualizar.geometry('300x300')

        lbl_numero = tk.Label(self.nova_janela_atualizar, text='Novo Número da Conta:')
        lbl_numero.pack(pady=5)
        self.ent_novo_numero_conta = tk.Entry(self.nova_janela_atualizar)
        self.ent_novo_numero_conta.pack(pady=5)
        self.ent_novo_numero_conta.insert(0, conta_selecionada.numero)

        lbl_titular = tk.Label(self.nova_janela_atualizar, text='Novo Titular da Conta:')
        lbl_titular.pack(pady=5)
        self.ent_novo_titular = tk.Entry(self.nova_janela_atualizar)
        self.ent_novo_titular.pack(pady=5)
        self.ent_novo_titular.insert(0, conta_selecionada.titular)

        lbl_saldo = tk.Label(self.nova_janela_atualizar, text='Novo Saldo:')
        lbl_saldo.pack(pady=5)
        self.ent_novo_saldo = tk.Entry(self.nova_janela_atualizar)
        self.ent_novo_saldo.pack(pady=5)
        self.ent_novo_saldo.insert(0, conta_selecionada.saldo)

        btn_salvar = tk.Button(self.nova_janela_atualizar, text='Salvar',
                               command=lambda: self.salvar_atualizacao_conta(conta_selecionada))
        btn_salvar.pack(pady=10)

    def salvar_atualizacao_conta(self, conta_selecionada):
        novo_numero = self.ent_novo_numero_conta.get()
        novo_titular = self.ent_novo_titular.get()
        novo_saldo = self.ent_novo_saldo.get()

        try:
            novo_saldo = float(novo_saldo)
        except ValueError:
            messagebox.showwarning('Atenção', 'Saldo inválido. Por favor, insira um número válido.')
            return

        if novo_numero and novo_titular:
            sistema.atualizar_conta(conta_selecionada, novo_numero, novo_titular, novo_saldo)
            messagebox.showinfo('Sucesso', 'Conta atualizada com sucesso!')
            self.nova_janela_atualizar.destroy()
            self.nova_janela_selecao.destroy()
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

    def cadastrar_conta_poupanca(self):
        self.nova_janela = tk.Toplevel(self.janela)
        self.nova_janela.title('Cadastrar Conta Poupança')
        self.nova_janela.geometry('300x200')

        lbl_numero = tk.Label(self.nova_janela, text='Número da Conta Poupança:')
        lbl_numero.pack(pady=5)
        self.ent_numero_conta = tk.Entry(self.nova_janela)
        self.ent_numero_conta.pack(pady=5)

        lbl_titular = tk.Label(self.nova_janela, text='Titular da Conta:')
        lbl_titular.pack(pady=5)
        self.ent_titular = tk.Entry(self.nova_janela)
        self.ent_titular.pack(pady=5)

        btn_salvar = tk.Button(self.nova_janela, text='Salvar', command=self.salvar_conta_poupanca)
        btn_salvar.pack(pady=10)

    # def acessar_conta(self):
    #     nova_janela = tk.Toplevel(self.janela)
    #     nova_janela.title('Minha Conta')
    #     nova_janela.geometry('300x200')
    #     lbl_conta_poupanca = tk.Label(nova_janela, text='Selecione sua Conta')
    #     lbl_conta_poupanca.pack(pady=10)

    def cadastrar_cliente(self):
        self.nova_janela = tk.Toplevel(self.janela)
        self.nova_janela.title('Cadastrar Cliente')
        self.nova_janela.geometry('300x200')

        lbl_nome_cliente = tk.Label(self.nova_janela, text='Nome do Cliente:')
        lbl_nome_cliente.pack(pady=5)
        self.ent_nome_cliente = tk.Entry(self.nova_janela)
        self.ent_nome_cliente.pack(pady=5)

        lbl_cpf = tk.Label(self.nova_janela, text='CPF do Cliente:')
        lbl_cpf.pack(pady=5)
        self.ent_cpf_cliente = tk.Entry(self.nova_janela)
        self.ent_cpf_cliente.pack(pady=5)

        btn_salvar = tk.Button(self.nova_janela, text='Salvar', command=self.salvar_cliente)
        btn_salvar.pack(pady=10)

    def salvar_cliente(self):
        nome = self.ent_nome_cliente.get()
        cpf = self.ent_cpf_cliente.get()
        if nome and cpf:
            sistema.cadastrar_cliente(nome, cpf)
            messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso!')
            self.nova_janela.destroy()
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

    def mostrar_cliente(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title('Clientes Cadastrados')
        nova_janela.geometry('300x200')

        lbl_clientes = tk.Label(nova_janela, text='Clientes Cadastrados:')
        lbl_clientes.pack(pady=10)

        listbox = tk.Listbox(nova_janela)
        listbox.pack(fill=tk.BOTH, expand=True)

        clientes = sistema.listar_clientes()
        if clientes:
            for cliente in clientes:
                listbox.insert(tk.END, f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}")
        else:
            listbox.insert(tk.END, "Nenhum cliente cadastrado.")

    def selecionar_cliente_para_atualizar(self):
        self.nova_janela_selecao = tk.Toplevel(self.janela)
        self.nova_janela_selecao.title('Selecionar Cliente para Atualizar')
        self.nova_janela_selecao.geometry('300x300')

        lbl_selecao = tk.Label(self.nova_janela_selecao, text='Selecione o Cliente:')
        lbl_selecao.pack(pady=10)

        self.listbox_clientes = tk.Listbox(self.nova_janela_selecao)
        self.listbox_clientes.pack(fill=tk.BOTH, expand=True)

        clientes = sistema.listar_clientes()
        if clientes:
            for cliente in clientes:
                self.listbox_clientes.insert(tk.END, f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}")
        else:
            self.listbox_clientes.insert(tk.END, "Nenhum cliente cadastrado.")

        btn_atualizar = tk.Button(self.nova_janela_selecao, text='Atualizar', command=self.atualizar_cliente)
        btn_atualizar.pack(pady=10)

    def atualizar_cliente(self):
        selecao = self.listbox_clientes.curselection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione um cliente para atualizar!")
            return

        index = selecao[0]
        cliente_selecionado = sistema.listar_clientes()[index]

        self.nova_janela_atualizar = tk.Toplevel(self.janela)
        self.nova_janela_atualizar.title('Atualizar Cliente')
        self.nova_janela_atualizar.geometry('300x200')

        lbl_nome = tk.Label(self.nova_janela_atualizar, text='Novo Nome do Cliente:')
        lbl_nome.pack(pady=5)
        self.ent_novo_nome_cliente = tk.Entry(self.nova_janela_atualizar)
        self.ent_novo_nome_cliente.pack(pady=5)
        self.ent_novo_nome_cliente.insert(0, cliente_selecionado['nome'])

        lbl_cpf = tk.Label(self.nova_janela_atualizar, text='Novo CPF do Cliente:')
        lbl_cpf.pack(pady=5)
        self.ent_novo_cpf_cliente = tk.Entry(self.nova_janela_atualizar)
        self.ent_novo_cpf_cliente.pack(pady=5)
        self.ent_novo_cpf_cliente.insert(0, cliente_selecionado['cpf'])

        btn_salvar = tk.Button(self.nova_janela_atualizar, text='Salvar',
                               command=lambda: self.salvar_atualizacao_cliente(cliente_selecionado))
        btn_salvar.pack(pady=10)

    def salvar_atualizacao_cliente(self, cliente_selecionado):
        novo_nome = self.ent_novo_nome_cliente.get()
        novo_cpf = self.ent_novo_cpf_cliente.get()
        if novo_nome and novo_cpf:
            sistema.atualizar_cliente(cliente_selecionado, novo_nome, novo_cpf)
            messagebox.showinfo('Sucesso', 'Cliente atualizado com sucesso!')
            self.nova_janela_atualizar.destroy()
            self.nova_janela_selecao.destroy()
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
