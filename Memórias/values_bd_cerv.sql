INSERT INTO Pessoa VALUES ('Joao', '1980-01-01', 'M', NULL);
INSERT INTO Pessoa VALUES ('Ze', '1980-01-01', 'M', NULL);
INSERT INTO Pessoa VALUES ('Pedro', '1980-01-01', 'M', NULL);
INSERT INTO Pessoa VALUES ('Paulo', '1980-01-01', 'M', NULL);
INSERT INTO Pessoa VALUES ('Carlos', '1980-01-01', 'M', NULL);
INSERT INTO Pessoa VALUES ('Jose', '1980-01-01', 'M', 'Joao');
INSERT INTO Pessoa VALUES ('Aiex', '1980-01-01', 'M', 'Aiex');
INSERT INTO Pessoa VALUES ('Joana', '1980-01-01', 'F', 'Aiex');
INSERT INTO Pessoa VALUES ('Ana', '1980-01-01', 'F', 'Aiex');

INSERT INTO Bar VALUES ('Braseiro', 'Sao Paulo', 'SP', 'Joao');
INSERT INTO Bar VALUES ('Mamae de Santo', 'Rio de Janeiro', 'RJ', 'Aiex');
INSERT INTO Bar VALUES ('Bar do Ze', 'Sao Paulo', 'SP', 'Ze');
INSERT INTO Bar VALUES ('Bar do Joao', 'Sao Paulo', 'SP', 'Joao');

INSERT INTO Cerveja VALUES ('Brahma', 'Pilsen', 'A', 'Brasil', 'Ambev');
INSERT INTO Cerveja VALUES ('Skol', 'Pilsen', 'A', 'Brasil', 'Ambev');
INSERT INTO Cerveja VALUES ('Antartica', 'Pilsen', 'A', 'Brasil', 'Ambev');
INSERT INTO Cerveja VALUES ('Heineken', 'Pilsen', 'A', 'Holanda', 'Heineken');
INSERT INTO Cerveja VALUES ('Corona', 'Pilsen', 'A', 'Mexico', 'Grupo Modelo');
INSERT INTO Cerveja VALUES ('Stella', 'Pilsen', 'A', 'Holanda', 'AB InBev');

INSERT INTO Gosta VALUES ('Joao', 'Brahma');
INSERT INTO Gosta VALUES ('Joao', 'Skol');
INSERT INTO Gosta VALUES ('Joao', 'Antartica');
INSERT INTO Gosta VALUES ('Joao', 'Heineken');
INSERT INTO Gosta VALUES ('Joao', 'Corona');

INSERT INTO Vende VALUES ('Braseiro', 'Brahma', 5);
INSERT INTO Vende VALUES ('Braseiro', 'Skol', 5);
INSERT INTO Vende VALUES ('Braseiro', 'Antartica', 5);
INSERT INTO Vende VALUES ('Braseiro', 'Heineken', 10);
INSERT INTO Vende VALUES ('Braseiro', 'Corona', 10);
INSERT INTO Vende VALUES ('Braseiro', 'Stella', 10);

INSERT INTO Vende VALUES ('Mamae de Santo', 'Brahma', 5);
INSERT INTO Vende VALUES ('Mamae de Santo', 'Skol', 5);
INSERT INTO Vende VALUES ('Mamae de Santo', 'Antartica', 5);
