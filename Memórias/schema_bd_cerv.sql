CREATE TABLE Cerveja(
Marca varchar(20),
Tipo varchar(20),
Cor char(1),
Pais varchar(20) DEFAULT('Brasil') NOT NULL,
Fabricante varchar(20),

CONSTRAINT PK_cerveja PRIMARY KEY (Marca),
CONSTRAINT CK_cerveja_cor CHECK (Cor IN ('A', 'M', 'P', 'C', 'D'))
); -- OK

CREATE TABLE Pessoa(
    Nome char(20),
    DataNasc date NOT NULL,
    Sexo char(1),
    Genitor char(20),

    CONSTRAINT PK_pessoa PRIMARY KEY (Nome),
    CONSTRAINT FK_pessoa_genitor FOREIGN KEY (Genitor) REFERENCES Pessoa(Nome)
); -- OK

CREATE TABLE Gosta(
    Pessoa char(20),
    Cerveja char(20),

    CONSTRAINT PK_gosta PRIMARY KEY (Pessoa, Cerveja),
    CONSTRAINT FK_gosta_pessoa FOREIGN KEY (Pessoa) REFERENCES Pessoa(Nome),
    CONSTRAINT FK_gosta_cerveja FOREIGN KEY (Cerveja) REFERENCES Cerveja(Marca)
); -- OK

CREATE TABLE Bar(
    Nome char(20),
    Cidade char(20),
    Estado char(20),
    Proprietario char(20),

    CONSTRAINT PK_bar PRIMARY KEY (Nome),
    CONSTRAINT FK_bar_proprietario FOREIGN KEY (Proprietario) REFERENCES Pessoa(Nome)
); -- OK

CREATE TABLE Vende(
    Bar char(20),
    Cerveja char(20),
    Valor int,

    CONSTRAINT PK_vende PRIMARY KEY (Bar, Cerveja),
    CONSTRAINT FK_vende_bar FOREIGN KEY (Bar) REFERENCES Bar(Nome),
    CONSTRAINT FK_vende_cerveja FOREIGN KEY (Cerveja) REFERENCES Cerveja(Marca)
); -- OK

