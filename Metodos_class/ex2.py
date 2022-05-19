'''

Classe Aluno

Atributos:
- ra
- nome
- lista_notas

metodos:
- inserir_nota
- calcular_media
'''


class Aluno:
    def __init__(self, ra, nome):               # construtor

        # atributos da classe
        self.ra = ra
        self.nome = nome
        self. lista_notas = []              # valor pré definido

        # métodos da classe
    def inserir_notas(self, nota):
        self.lista_notas.append(nota)

    def calcular_media(self):
        media = sum(self.lista_notas) / len(self.lista_notas)
        return media


aluno1 = Aluno(123456, "Daniel")
aluno1.inserir_notas(8)
aluno1.inserir_notas(9)
aluno1.inserir_notas(6)
print(aluno1.lista_notas)
print(aluno1.calcular_media())

aluno2 = Aluno(4567890, "Julia")
aluno2.inserir_nota(6)
aluno2.inserir_nota(7)
print(aluno2.inserir_nota)
