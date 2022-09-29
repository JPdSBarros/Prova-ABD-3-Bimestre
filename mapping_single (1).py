from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine

def auto (nome_t, estadio_t, capacidade_e, cidade_t, Session):
    with Session.begin() as session:
        time = TimeRugby(
            nome = nome_t,
            estadio = estadio_t,
            capacidade = capacidade_e,
            cidade = cidade_t)
        session.add(time)
        



URL="mysql+mysqlconnector://aluno:aluno123@127.0.0.1:3306/intro_orm"
engine = create_engine(url=URL)

Base = declarative_base()

class TimeRugby(Base):
    __tablename__ = "time_rugby"
    id_time = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    estadio = Column(String(150), nullable=False)
    capacidade = Column(Integer, nullable=True)
    cidade = Column(String(150), nullable=False)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

auto(nome_t = "Jacareí Rugby ", estadio_t = "Toca do Jacaré", capacidade_e = 200, cidade_t= "Jacareí/SP - Brasil", Session = Session)
auto(nome_t = "BH Rugby", estadio_t = "BH Stadium", capacidade_e = 300, cidade_t= "Belo Horizonte/MG - Brasil",  Session = Session)
auto(nome_t = "Inconfidentes Rugby ", estadio_t = "A.A.A", capacidade_e = 500, cidade_t= "Ouro Preto/MG - Brasil", Session = Session)
auto(nome_t = "Taurus Rugby ", estadio_t = "Tauru Stadium", capacidade_e = 200, cidade_t= "Uberaba/MG - Brasil",  Session = Session)
auto(nome_t = "Uberlândia Rugby Clube ", estadio_t = "Uberl Stadium", capacidade_e = 350, cidade_t= "Uberlândia/MG - Brasil",  Session = Session)
auto(nome_t = "São Paulo Atlhetic Club - SPAC", estadio_t = "Praça de Esportes Charles Miller", capacidade_e = 550, cidade_t= "São Paulo/SP - Brasil",  Session = Session)
auto(nome_t = "Pasteur Athlétique Club", estadio_t = "Liceu Pasteur", capacidade_e = 560, cidade_t= "São Paulo/SP - Brasil",  Session = Session)
auto(nome_t = "Federal Rugby Club", estadio_t = "Campo Atibaia", capacidade_e = 245, cidade_t= "Atibaia/SP - Brasil",  Session = Session)
auto(nome_t = "Medicina Rugby", estadio_t = "Med Stadium", capacidade_e = 250, cidade_t= "São Paulo/SP - Brasil",  Session = Session)
auto(nome_t = "Rugby São Carlos", estadio_t = " Campo da USP São Carlos", capacidade_e = 250, cidade_t= "São Carlos/SP - Brasil",  Session = Session)


'''
with Session.begin() as session:
    time = TimeRugby(
        nome = "Jacareí Rubgy - JAC",
        estadio = "Toca do Jacaré",
        capacidade = 200,
        cidade = "Jacareí/SP -  Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = "BH Rugby",
        estadio = "BH Stadium",
        capacidade = 200,
        cidade = "Belo Horizonte/MG -  Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = "Inconfidentes Rugby",
        estadio = "	Campo da Associação Atlética Aluminas - A.A.A.",
        capacidade = 200,
        cidade = "Ouro Preto/MG - Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = "Taurus Rugby",
        estadio = "	Tauru Stadium",
        capacidade = 200,
        cidade = "Uberaba/MG - Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = "Uberlândia Rugby Clube",
        estadio = "	Uber Stadium",
        capacidade = 200,
        cidade = "Uberlândia/MG - Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = " São Paulo Athletic Club - SPAC",
        estadio = "Praça de Esportes Charles Miller",
        capacidade = 200,
        cidade = "São Paulo/SP - Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = " 	Pasteur Athlétique Club",
        estadio = "	Liceu Pasteur ",
        capacidade = 200,
        cidade = "São Paulo/SP - Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = " 	Federal Rugby Club",
        estadio = "  Campo-sede em Atibaia-SP",
        capacidade = 200,
        cidade = "Atibaia/SP - Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = " 	Medicina Rugby",
        estadio = " Med Stadium ",
        capacidade = 200,
        cidade = "São Paulo/SP - Brasil"

    )
    session.add(time)

with Session.begin() as session:
    time = TimeRugby(
        nome = " 	Rugby São Carlos ",
        estadio = " Campo da USP São Carlos ",
        capacidade = 200,
        cidade = "São Carlos/SP - Brasil"

    )
    session.add(time)
'''