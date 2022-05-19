# EXEMPLO:
# Criar dicionario para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {1234567: 'Paulo', 
            7896567: 'Maria', 
            5556666: 'Gabriel'}

# Imprimir dicionário
print(cadastro)

# Imprimir item do dicionário (acesso pela chave)
print(cadastro[1234567])

# Adicionar item no dicionario
cadastro[9999999] = 'Fernando'
print(cadastro)

# Alterar item do dicionário
cadastro[9999999] = 'Fernando da Silva'
print(cadastro)

# Excluir item do dicionário (função pop)
cadastro.pop(1234567)
print(cadastro)

# Verificar se chave existe no dicionário
if 345678 in cadastro:
    print(cadastro[345678])
else:
    print('CPF não cadastrado')

# Percorrer o dicionario com estrutura de repetição
for a in cadastro:      # percorre as chaves
    print(a)

for a in cadastro:      # percorre os valores
    print(cadastro[a])

for a in cadastro:      # percorre as chaves e os valores
    print(a, cadastro[a])

# Percorre os item de forma crescente pela chave
print('Ordem crescente: ')
chaves = sorted(cadastro)
for c in chaves:
    print(c, cadastro[c])


# preencher dicionário com dados informados pelo usuário
cadastro = {}
while True:
    cpf = input('CPF: ')
    if cpf == '':           # finaliza se usuario só der um enter
        break
    cpf = int(cpf)          # converte cpf para int
    nome = input('Nome: ')
    if cpf in cadastro:
        print('CPF já cadastrado')
    else:
        cadastro[cpf] = nome
print(cadastro)
