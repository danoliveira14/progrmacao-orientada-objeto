'''
Classe cachorro

Atributos (caracteristicas):
- nome
- idade

Metodos (comportamentos):
- andar
- comer
- latir
'''


class Cachorro:
    def __init__(self, nome, idade):                  # metodo contrutor
        self.nome = nome
        self.idade = idade

    def andar(self):
        print('o cachorro', self.nome,  'esta andando')

    def comer(self):
        print('o cachorro', self.nome,  ' esta comendo')

    def latir(self):
        print('o cachorro', self.nome,  ' esta latindo')

    def exibir(self):
        print('nome', self.nome)
        print('Idade', self.idade)


cachorro1 = Cachorro("tobi", 5)                # cria um objeto
cachorro1.idade = 6                       # alterando atributo
cachorro1.andar()                        # executa os metodos
cachorro1.comer()
cachorro1.latir()

nome = input("Nome do cachorro: ")
idade = int(input("Idade do cachorro: "))
cachorro2 = Cachorro(nome, idade)


# cachorro2 = Cachorro("Doguinho", 2)            # cria outro objeto
cachorro2.andar()
cachorro1.exibir()                           # exibe as informações do cachorro
