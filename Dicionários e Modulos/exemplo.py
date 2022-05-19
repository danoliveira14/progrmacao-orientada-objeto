# importação relativa
from math import sqrt, factorial
from random import randint, choice
from modulo1 import soma, exibe_numeros

n = sqrt(30)
print(n)

n = factorial(5)
print(n)

n = randint(1, 50)          # sorteia um numero inteiro
print(n)

texto = 'abcdefghijk'
x = choice(texto)           # sortei um caracter da string
print(x)

lista = [5, 4, 7, 10, 20]   # sorteia um item da lista
x = choice(lista)
print(x)

x = soma(3, 10)
print(x)

x = exibe_numeros(6, 20)
print(x)
