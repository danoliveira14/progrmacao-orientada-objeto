'''
Preencha um dicionário com as informações de 5 produtos.
Utilize o nome do produto como chave e o preço como valor.
Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00
'''

produtos = {}
while True:
    nome = input('Nome do produto: ')
    if nome == '':              # finaliza o loop quando o usuario nao informar o nome
        break
    preco = float(input('Preço do produto: '))
    produtos[nome] = preco      # insere os dados no dicionario

print(produtos)                 # exibe o dicionario

for chave in produtos:          # percorre o dicionarios
    if produtos[chave] > 50:    # verifica o preço de cada produto
        print(chave, produtos[chave])


