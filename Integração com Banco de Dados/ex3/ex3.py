'''
Crie as tabelas abaixo no banco de dados SQLITE e faça o mapeamento dessas tabelas utilizando o SQLAlchemy.
Implementar um programa para realizar as seguintes operações:
Cadastrar um médico.
Cadastrar dois pacientes.
Cadastrar dois exames (um para cada paciente).
Inserir os dados cadastrados banco de dados.
Realizar uma consulta no banco de dados para verificar se os dados foram inseridos corretamente.

Scripts para criação das tabelas no banco de dados:
connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CPF VARCHAR(255),
                        IDADE INTEGER)""")

connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")
'''

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///ex2/server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CPF VARCHAR(255),
                        IDADE INTEGER)""")

connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")

class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String(255))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', String(255))
    especializacao = Column('ESPECIALIZACAO', String(255))

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    id_medico = Column('ID_MEDICO', Integer)
    id_paciente = Column('ID_PACIENTE', Integer)
    descricao = Column('DESCRICAO', String(255))
    resultado = Column('RESULTADO', String(255))

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado



medico1 = Medico('Zezinho', 234340, 'oftalmo')
session.add(medico1)                       # insere os dados de um objeto
session.commit()                        # necessario fazer o commit()



# Inserir uma lista de objetos
pacien1 = Paciente('Luizinho', "454.656.645-3", 33)
pacien2 = Paciente('Huguinho', '343.322.553-6', 77)
lista = [pacien1, pacien2]
session.add_all(lista)                  # insere os dados de todos os objetos
session.commit()

# Inserir uma lista de objetos
exame1 = Exame(medico1.id, pacien1.id, "ta com o cu doendo", "operar o boga")
exame2 = Exame(medico1.id, pacien2.id, "perdeu o olho", "vai botar olho de vidro")
lista = [exame1, exame2]
session.add_all(lista)                  # insere os dados de todos os objetos
session.commit()


print('-'*20, 'Medicos:')
resultado_medico = session.query(Medico)
for obj in resultado_medico:
    print(obj.id, obj.nome, obj.crm, obj.especializacao)


print('-'*20, 'Paciente:')
resultado_paciente = session.query(Paciente)
for obj in resultado_paciente:
    print(obj.id, obj.nome, obj.cpf, obj.idade)


print('-'*20, 'Exame:')
resultado_exame = session.query(Exame)
for obj in resultado_exame:
    print(obj.id, obj.id_medico, obj.id_paciente, obj.descricao, obj.resultado)



print('-'*20, 'Exame JOIN:')
resultado_exame = session.query(Exame, Paciente, Medico).filter(Exame.id_paciente == Paciente.id, Exame.id_medico == Medico.id)
for obj in resultado_exame:
    print(obj.Exame.id, obj.Medico.nome, obj.Paciente.nome, obj.Exame.descricao, obj.Exame.resultado)

# -----------------------------------------------------------------------------
# FECHANDO CONEXÃO COM BANCO DE DADOS
connection.close()

