CREATE DATABASE IF NOT EXISTS orm_programa_clubes;

USE orm_programa_clubes;


CREATE TABLE IF NOT EXISTS Pessoa (
    cpf  INTEGER      PRIMARY KEY,
    nome       VARCHAR(100) NOT NULL,
    natalidade DATE         NOT NULL
);

CREATE TABLE IF NOT EXISTS Telefones (
    id_telefone  INTEGER      PRIMARY KEY AUTO_INCREMENT,
    cpf    INTEGER  NOT NULL,
    numero INTEGER  NOT NULL,
    CONSTRAINT fk_PesTel FOREIGN KEY (cpf) REFERENCES Pessoa (cpf)
);

CREATE TABLE IF NOT EXISTS Membros (
    id_membro  INTEGER      PRIMARY KEY AUTO_INCREMENT,
    cpf   INTEGER NOT NULL,
    data_integracao DATE         NOT NULL,
    CONSTRAINT fk_PesMem FOREIGN KEY (cpf) REFERENCES Pessoa (cpf)
);


CREATE TABLE IF NOT EXISTS Donos (
    id_dono  INTEGER      PRIMARY KEY AUTO_INCREMENT,
    cpf   INTEGER NOT NULL,
    data_integracao DATE    NOT NULL,
    CONSTRAINT fk_PesDon FOREIGN KEY (cpf) REFERENCES Pessoa (cpf)
);

CREATE TABLE IF NOT EXISTS Locais (
    CNPJ  INTEGER      PRIMARY KEY AUTO_INCREMENT,
    nome       VARCHAR(100) NOT NULL,
    endereço   VARCHAR(100) NOT NULL,
    horarios   DATE NOT NULL

);


CREATE TABLE IF NOT EXISTS Clubes (
    id_Clube  INTEGER      PRIMARY KEY AUTO_INCREMENT,
    nome       VARCHAR(100) NOT NULL,
    id_dono INTEGER     NOT NULL,
    data_criacao DATE   NOT NULL,
    quantidade_membros INTEGER NOT NULL,
    locais INTEGER NOT NULL

    CONSTRAINT fk_clubdon FOREIGN KEY (id_dono) REFERENCES Donos (id_dono)
    CONSTRAINT fk_clubloc FOREIGN KEY (locais) REFERENCES Locais(cnpj)
);

 
 
