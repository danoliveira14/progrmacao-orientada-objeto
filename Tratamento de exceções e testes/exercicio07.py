'''
Crie um dicionário para armazenar uma listagem de alunos.
Utilize como chave o RA do aluno e como valor o nome do aluno.
O RA de cada aluno deve ser composto por um número inteiro
de exatamente 7 dígitos.
Caso o RA informado não esteja no formato correto, deve ser gerada
uma exceção do tipo ValueError (utilize a instrução raise).
Caso o RA informado já exista no dicionário, deve ser gerada uma
exceção do tipo TypeError (utilize a instrução raise).
'''

alunos = {}
for i in range(5):
    try:
        ra = input('RA: ')
        if len(ra) != 7:            # verifica se o RA tem 7 caracteres
            raise ValueError        # gera uma exceção
        ra = int(ra)                # converte o RA para inteiro
        if ra in alunos:            # verifica se o ra ja está cadastrado
            raise TypeError         # gera uma exceção
        nome = input('Nome: ')
        alunos[ra] = nome
    except ValueError:
        print('O RA nao tem 7 dígitos')
    except TypeError:
        print('O RA já está cadastrado')
print(alunos)
