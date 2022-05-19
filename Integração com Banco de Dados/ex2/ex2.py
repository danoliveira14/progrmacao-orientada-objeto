'''
Implementar um programa em Python que realize as seguintes operações:

Conectar com o banco de dados SQLITE e criar as tabelas AUTOR e LIVRO (utilize os scripts abaixo para a criação das tabelas).
Criar as classes Autor e Livro e fazer o mapeamento das tabelas.
Inserir nas tabelas dois autores e dois livros.
Fazer uma consulta para verificar se os dados foram inseridos corretamente. 

Scripts para criação das tabelas no banco de dados:
connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")
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

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")

class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)

    def __init__(self, nome):
        self.nome = nome

class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255), nullable=False)
    paginas = Column('PAGINAS', Integer, nullable=False)
    autor_id = Column('AUTOR_ID', Integer, nullable=False)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id

# INSERINDO AUTORES
autor1 = Autor('Felipe')
autor2 = Autor('Igor')
lista = [autor1, autor2]
session.add_all(lista)
session.commit()

# INSERINDO lIVROS
livro1 = Livro('livrinho legal', 84, autor2.id)
livro2 = Livro('livrão dahora', 96, autor2.id)
lista = [livro1, livro2]
session.add_all(lista)
session.commit()

print('-'*20, 'AUTORES CADASTRADOS')
resultado_autor = session.query(Autor)
for obj in resultado_autor:
    print(obj.nome)

print('-'*20, 'LIVROS CADASTRADOS')
resultado_livros = session.query(Livro)
for obj in resultado_livros:
    print(obj.titulo, obj.paginas, obj.autor_id)

# -----------------------------------------------------------------------------
# FECHANDO CONEXÃO COM BANCO DE DADOS
connection.close()