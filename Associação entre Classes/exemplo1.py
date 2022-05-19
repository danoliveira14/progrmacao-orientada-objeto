class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        #atributos publicos
        self.nome = nome
        self.idade = idade

        #atributos privados
        self.__cpf = cpf
        self.__rg = rg

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg


    def set_cpf(self, cpf):
        if self.__validar_cpf(cpf):
            self.__cpf = cpf


    def set__rg(self, rg):        
        self.__rg = rg


        #metodo privado
    def __validar_cpf(self, cpf):
        if type(cpf) == str and len(cpf) == 11:
            return True
        else:
            if type(cpf) != str:
                print("CPF Invalido tem que ser uma String")
            elif len(cpf) > 11 or len(cpf) < 11:
                print('CPF Invalido: é necessario que o CPF tenha 11 Caracteres')
            return False


pessoa = Pessoa ("João", 25, "111111111", "3333333333")

print("Nome: ", pessoa.nome)    #exibe o nome da pessoa
print("CPF: ", pessoa.get_cpf())        #exibe CPF da pessoa 

pessoa.idade = 17                           #altera a idade da pessoa
pessoa.set_cpf(222)                   #altera o CPf  
pessoa.nome = "daniel"


print("Nome: ", pessoa.nome)
print("CPF: ", pessoa.get_cpf())

