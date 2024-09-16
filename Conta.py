class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R${valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: R${valor:.2f}")
            return True
        return False

    def mostrar_saldo(self):
        return self.saldo

    def mostrar_historico(self):
        return "\n".join(self.historico)


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0.0, taxa_juros=0.005):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros  # taxa de juros a 0,005

    def atualizar_saldo(self):
        self.saldo += self.saldo * self.taxa_juros
        self.historico.append(f"Atualização de Saldo: +R${self.saldo * self.taxa_juros:.2f}")
class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0.0, taxa_desconto=1.0):
        super().__init__(numero, titular, saldo)
        self.taxa_desconto = taxa_desconto  # desconto de 1 real por operação

    def depositar(self, valor):
        if super().depositar(valor):
            self.saldo -= self.taxa_desconto  # desconta ao depositar
            self.historico.append(f"Desconto por depósito: -R${self.taxa_desconto:.2f}")
            return True
        return False

    def sacar(self, valor):
        if super().sacar(valor):
            self.saldo -= self.taxa_desconto  # desconta ao sacar
            self.historico.append(f"Desconto por saque: -R${self.taxa_desconto:.2f}")
            return True
        return False