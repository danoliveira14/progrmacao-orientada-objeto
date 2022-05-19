# Realizar a divisão de doisnumeros inteiros positivos
# Identificar e tratar os possiveis erros.
# exemplo 1
try:
    a = int(input("Entre com numero: "))
    b = int(input("Entre com outro numero: "))
    if a < 0 or b < 0:
        raise TypeError      # provoca exceção 
    c = a / b
    print("Resultado: ", c)
except TypeError:
     print("Erro. o numero informado não é positivo")   
except ZeroDivisionError:
    print("Ops, segundo numero não pode ser zero!")
except ValueError:
    print("O valor informado é de um tipo inválido!")
except Exception:
    print("Erro inesperado")
else:
    print("operação realizada com sucesso")    




