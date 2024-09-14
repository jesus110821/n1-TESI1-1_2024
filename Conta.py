class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0.0):
        super().__init__(numero, titular, saldo)