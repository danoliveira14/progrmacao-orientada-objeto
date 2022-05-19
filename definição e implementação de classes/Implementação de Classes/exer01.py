'''
Exercício 01

Nome da classe:
Carro

Atributos:
marca
modelo
placa

Métodos:
__init__(self, marca, modelo, placa): Método construtor
exibir_dados(self): Deve exibir os valores dos atributos do carro

No programa principal:
Crie dois objetos da classe Carro
Utilize o método exibir_dados para exibir no terminal os atributos dos carros.
'''



class Carro:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print('-'*80)
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Placa: ', self.placa)


carro1 = Carro('Ford', 'Ka', 'QBC-1234')
carro2 = Carro('Fiat', 'Siena', 'FGT-5065')

carro1.exibir_dados()
carro2.exibir_dados()
