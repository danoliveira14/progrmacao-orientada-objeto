'''

Exercício 03

Implemente as classes ContaBancaria e Cliente, conforme o diagrama de classes abaixo.

Classe Cliente
Atributos::
nome: nome do cliente (público)
cpf: cpf do cliente (privado)
senha: senha do cliente (privado)
Métodos:
get_senha: retorna a senha do cliente


Classe ContaBancaria
Atributos:
numero: numero da conta (público) 
cliente: objeto Cliente associado à conta (público)
saldo: saldo da conta (privado). Deve ser inicializado com zero.
Métodos:
get_saldo: retorna o saldo da conta.
depositar: recebe como parâmetros de entrada um valor e uma senha. Acrescenta esse valor ao saldo da conta apenas se a senha for igual à senha do cliente.
sacar: recebe como parâmetros de entrada um valor e uma senha. Subtrai esse valor do saldo da conta, apenas se a senha for igual à senha do cliente.

Utilize o código abaixo para testar as suas classes
cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo())            # Imprime 150

'''

class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha

class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
        else:
            print('Senha Invalida')
    
    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            if self.__saldo > valor:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente')
            
        else:
            print('Senha Invalida')

cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print('Seu saldo é de: R$', conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print('Seu saldo é de: R$', conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print('Seu saldo é de: R$', conta.get_saldo())            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print('Seu saldo é de: R$', conta.get_saldo())            # Imprime 150
