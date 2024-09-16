class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0.0):
        super().__init__(numero, titular, saldo)