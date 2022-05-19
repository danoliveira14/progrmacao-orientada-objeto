'''
Nome da classe
    ContaBancaria
Atributos:
    numero
    titular
    senha
    saldo (deve ser inicializado no construtor com o valor zero)
Métodos:
    __init__(self, numero, titular, senha)
    depositar(self, valor, senha)
    sacar(self, valor, senha)
'''


class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0              # valor inicial

    def depositar(self, valor, senha):
        if senha == self.senha:         # valida a senha
            self.saldo += valor
            print('Deposito realizado com sucesso!!')
        else:
            print('ERRO. Senha inválida!!')

    def sacar(self, valor, senha):
        if senha == self.senha:         # valida a senha
            self.saldo -= valor
            print('Saque realizado com sucesso!!')
            return True
        else:
            print('ERRO. Senha inválida')
            return False


# cria uma conta
conta = ContaBancaria(456231, 'Paulo Vieira', 123456)
print('Saldo:', conta.saldo)

conta.depositar(300, 123456)            # realiza deposito

# realiza um saque (três tentativas de senha)
tentativas = 0
while tentativas < 3:
    valor = float(input('Valor de saque: '))
    senha = int(input('Informe a senha: '))
    if conta.sacar(valor, senha):
        break               # sai do while quando conseguir realizar o saque
    else:
        tentativas += 1     # incrementa as tentativas a cada erro

print('Saldo:', conta.saldo)
