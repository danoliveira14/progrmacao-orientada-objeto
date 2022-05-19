'''
Nome da classe
    Aluno
Atributos:
    ra
    nome
    turma
    notas (lista que deve ser inicializada como vazia)
Métodos:
    __init__(self, ra, nome, turma)
    inserir_nota(self, nota)
    calcular_media(self)

Crie 3 objetos da classe aluno. Insira algumas notas para os alunos.
Insira os objetos em uma lista.
Percorra a lista, calcule e exiba a média aritmética de cada aluno.
'''


class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []

    def inserir_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
        else:
            print('Nota inválida')

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)


# cria tres objetos
aluno1 = Aluno(1234567, 'Paulo', 'SI2A')
aluno2 = Aluno(5678789, 'Maria', 'SI2A')
aluno3 = Aluno(5555666, 'João', 'SI2A')

# insere as notas dos alunos
aluno1.inserir_nota(9)
aluno1.inserir_nota(6)

aluno2.inserir_nota(8)
aluno2.inserir_nota(7)

aluno3.inserir_nota(9.5)

# insere alunos em uma lista
lista = [aluno1, aluno2, aluno3]

# percorre a lista de alunos
for x in lista:
    print(x.nome, x.calcular_media())   # calcula media