'''
Exercício 02

Nome da classe:
Funcionario

Atributos:
nome
sobrenome
salario

Métodos:
__init__(self, nome, sobrenome, salario): Método construtor. Deve fazer uma validação do salário e, se o salário informado for negativo, deve definí-lo como zero.
aumentar_salario(self): Aumentar o salário do funcionário em 10%.


No programa principal:
Crie dois objetos da classe Funcionario
Utilize o método aumentar_salario para atualizar os salários dos funcionários.
'''


class Funcionario:
    def __init__(self, nome, sobrenome, salario_mensal):
        self.nome = nome
        self.sobrenome = sobrenome
        if salario_mensal > 0:
            self.salario_mensal = salario_mensal
        else:
            self.salario_mensal = 0

    def aumentar_salario(self):
        self.salario_mensal += self.salario_mensal * 0.10


func = Funcionario('Daniel', 'oliveira', 2000)
func.aumentar_salario()
print('Nome:', func.nome, func.sobrenome)
print('Salario:', func.salario_mensal)
