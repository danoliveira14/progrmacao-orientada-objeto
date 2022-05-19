from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# Criar Conexão com Banco SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine('sqlite:///servidor.db')
connection = engine.connect()

# Criar sessão com o Banco de Dados
session = Session()

# Instância da classe Base do SQLAlchemy
Base = declarative_base(engine)

connection.execute('''CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)''')


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


# Abre o arquivo de texto
arquivo = open('funcionarios.txt', 'r', encoding='UTF-8')

lista_funcionario = []

# percorre o arquivo de texto
for linha in arquivo:

    # separa linha pelo caracter ';' e gera lista [nome, idade, salario]
    lista = linha.split(';')

    # cria um objeto Funcionario
    func = Funcionario(lista[0], int(lista[1]), float(lista[2]))

    # insere o objeto na lista
    lista_funcionario.append(func)

# insere lista de objetos no banco de dados
session.add_all(lista_funcionario)
session.commit()

# Consulta os dados cadastrados
funcionarios = session.query(Funcionario)
for f in funcionarios:
    print(f.id, f.nome, f.idade, f.salario)

arquivo.close()
connection.close()