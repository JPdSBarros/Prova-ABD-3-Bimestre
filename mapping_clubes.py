from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

URL="mysql+mysqlconnector://localhost/intro_orm"
engine = create_engine(url=URL)

Base = declarative_base(orm_programa_clubes)

class Pessoa(Base):
    __tabela__ = "Pessoa"
    cpf = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    natalidade = Column(Date, nullable=False)
    

class Telefone(Base):
    __tabela__ = "telefones"
    id_telefone = Column(Integer, primary_key=True)
    cpf = Column(Integer, nullable=False)
    numero = Column(Integer, nullable=False) 

class Dono(Base):
    __tabela__ = "Donos"
    id_dono = Column(Integer, primary_key=True)
    cpf = Column(Integer, nullable=False)
    data_integracao = Column(Date, nullable=False)
    

class Membro(Base):
    __tabela__ = "Membros"
    id_membro = Column(Integer, primary_key=True)
    cpf = Column(Integer, nullable=False)
    data_integracao = Column(Date, nullable=False)
    

class Clube(Base):
    __tabela__ = "Clubes"
    id_Clube = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    id_dono = Column(Integer, nullable=False)
    quantidade_membros = Column(Integer, nullable=False)
    locais= Column(Integer, nullable=False)
    

class Local(Base):
    __tabela__ = "Locais"
    CNPJ = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    endereço = Column(String(100), nullable=False) 
    horarios = Column(Date,nullable=False)
    
Base.metadata.create_all(engine)

cx = engine.connect()
rs = cx.execute("SELECT COUNT(*) FROM Menbros")
