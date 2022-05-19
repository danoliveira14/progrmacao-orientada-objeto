'''
Preencha um dicionário com os dados de 5 alunos.
Utilize o ra do aluno como chave e uma lista de três notas como valor.
Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.
'''

alunos = {}
while True:
    ra = input('RA: ')
    if ra == '':
        break
    ra = int(ra)        # converta a string para inteiro
    lista = []
    for n in range(3):
        nota = float(input('Informe uma nota: '))
        lista.append(nota)
    alunos[ra] = lista

print(alunos)

for chave in alunos:                    # percorre o dicionario
    media = sum(alunos[chave]) / len(alunos[chave])     # calcula a media
    print(chave, media)

    


