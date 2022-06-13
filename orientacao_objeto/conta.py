class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato (self):
        print(f"""{self.titular}
Conta: {self.numero}
Saldo: {self.saldo}""")

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        elif (self.limite + self.saldo) >= valor:
            valor -= self.saldo
            self.saldo = 0
            self.limite -= valor
        else:
            print("Saldo insuficiente")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
