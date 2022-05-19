'''

Exercício 02

Implemente a classe Filme, conforme o diagrama de classes abaixo
Todos os atributos devem ser privados
Crie os métodos get e set para todos os atributos

No seu programa principal, faça a seguinte implementação:
Criar uma lista de filmes vazia
Cadastrar 3 filmes (com os dados informados pelo usuário)
Armazenar os objetos na lista de filmes
Percorrer a lista de filmes e imprimir no terminal os dados de todos os filmes cadastrados



'''

class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero
    
    # GETTERS
    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero
    
    # SETTERS
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_genero(self, genero):
        self.__genero = genero

filmes = []

for i in range(3):
    filme = Filme(input('Informe o titulo: '), input('Informa o Genero: '))

    filmes.append(filme)



for filme in filmes:
    print(f'Titulo: {filme.get_titulo()}')
    print(f'Genero: {filme.get_genero()}')
    print('--------------------------------')