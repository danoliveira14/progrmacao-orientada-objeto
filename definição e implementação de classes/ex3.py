

class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

        # metodos da classe

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print("Saldo da conta: ", self.saldo)


numero = int(input("numero da conta: "))
titular = input("nome do titular: ")
conta1 = ContaBancaria(numero, titular)        # cria o objeto

conta1.exibir_saldo()
conta1.depositar(200)
conta1.sacar(80)
conta1.exibir_saldo()
