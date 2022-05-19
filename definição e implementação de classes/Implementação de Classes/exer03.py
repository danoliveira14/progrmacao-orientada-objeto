'''
Exercício 03

Nome da Classe:
ContaBancaria

Atributos:
    numero
    titular
    senha
    saldo (deve ser inicializado no construtor com o valor zero)

Métodos:
    __init__(self, numero, titular, senha):
Método construtor.

    depositar(self, valor, senha):
Deve verificar se a senha informada está correta.
Se estiver, deve realizar a operação de deposito e atualizar o saldo da conta.
Caso contrário deve exibir uma mensagem de senha incorreta.

    sacar(self, valor, senha):
Deve verificar se a senha informada está correta.
Se estiver, deve realizar a operação de saque e atualizar o saldo da conta.
Caso contrário deve exibir uma mensagem de senha incorreta.

No programa principal:
Crie um objeto da classe ContaBancaria
Realize operações de depósito e saque utilizando
os métodos implementados na clase.
'''


class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0                       # Valor inicial

    def depositar(self, valor, senha):
        if senha == self.senha:             # valida a senha
            self.saldo += valor
            print('Deposito realizado com sucesso!')
        else:
            print('ERRO. Senha invalida')

    def sacar(self, valor, senha):
        if senha == self.senha:             # valida a senha
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print('ERRO. Senha invalida')


# Criar uma conta

conta = ContaBancaria(493843, 'Daniel Oliveira', 123456)
print("Saldo:", conta.saldo)

# Realizar um deposito

valor = float(input('Valor de deposito: '))
senha = int(input('Informe a senha: '))
conta.depositar(valor, senha)
print('Saldo:', conta.saldo)

# realiza saque

valor = float(input('Valor de saque: '))
senha = int(input('Informe a senha: '))
conta.sacar(valor, senha)
print('Saldo:', conta.saldo)
