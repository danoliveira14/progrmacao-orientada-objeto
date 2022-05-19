'''
Exercício 1

Implementar um programa em Python que realize as seguintes operações:

. Conectar com o banco de dados SQLITE e criar a tabela FUNCIONARIO (utilize o script abaixo para a criação da tabela).
. Criar uma classe Funcionario e mapear a tabela criada anteriormente.
. Instanciar três objetos da classe Funcionario.
. Inserir os dados dos objetos na tabela. 
. Realizar uma consulta na tabela de funcionários e verificar se os dados foram inseridos corretamente.
. Realizar uma consulta na tabela de todos os funcionários com salário superior a R$ 1.500,00.

Scripts para criação das tabelas no banco de dados:
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""")

'''


# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///ex1/server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""")

# DEFINIÇÃO DE CLASSE QUE MAPEIA UMA TABELA
class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)
    salario = Column('SALARIO', Float, nullable=False)

    def __init__(self, nome, idade, salario):   # Método construtor da classe
        self.nome = nome
        self.idade = idade
        self.salario = salario

func1 = Funcionario('daniel', 23, 4500)
func2 = Funcionario('igor', 20, 500)
func3 = Funcionario('scarpa', 45, 3200)

lista = [func1, func2, func3]

session.add_all(lista)
session.commit()

print('-'*10, 'TODOS OS FUNCIONARIOS CADASTRADOS')
resultado = session.query(Funcionario)
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)

print('-'*10, 'TODOS OS FUNCIONARIOS CADASTRADOS COM O SALARIO SUPERIOR A 1500')
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500)
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)

# -----------------------------------------------------------------------------
# FECHANDO CONEXÃO COM BANCO DE DADOS
connection.close()
