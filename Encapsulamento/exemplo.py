class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        # atributos públicos
        self.nome = nome
        self.idade = idade
        # atributos privados
        self.__cpf = cpf
        self.__rg = rg

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def set_cpf(self, cpf):
        if self.__validar_cpf(cpf):
            self.__cpf = cpf

    def set_rg(self, rg):
        self.__rg = rg

    # metodo privado
    def __validar_cpf(self, cpf):
        if type(cpf) == str and len(cpf) == 11:
            return True
        else:
            print('CPF invalido')
            return False


pessoa1 = Pessoa("João", 25, "11111111111", "3333333")

print("Nome: ", pessoa1.nome)       # Exibe nome da pessoa
print("CPF:", pessoa1.get_cpf())    # Exibe CPF da pessoa

pessoa1.idade = 26                  # Altera idade da pessoa
pessoa1.set_cpf('33333333333')      # Altera cpf da pessoa

print("Nome: ", pessoa1.nome)       # Exibe nome da pessoa
print("CPF:", pessoa1.get_cpf())    # Exibe CPF da pessoa
