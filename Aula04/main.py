import sqlite3

banco = sqlite3.connect('database.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoa( nome TEXT NOT NULL, nascimento DATE NOT NULL, oculos BOOLEAN NOT NULL, cpf INTEGER PRIMARY KEY)")
#cursor.execute("CREATE TABLE marca( id INTEGER PRIMARY KEY, nome TEXT NOT NULL, sigla CHARACTER(2) NOT NULL)")
#cursor.execute("CREATE TABLE veiculo( placa CHARACTER(7) NOT NULL, ano INTEGER NOT NULL, cor TEXT NOT NULL, proprietario INTEGER NOT NULL, marca INTEGER NOT NULL, PRIMARY KEY (placa), FOREIGN KEY(proprietario) REFERENCES pessoa(cpf), FOREIGN KEY(marca) REFERENCES marca(id))")
#cursor.execute("INSERT INTO pessoa (nome, nascimento, oculos, cpf) VALUES ('Cainã', '2004-06-10', true, 09101149350)")
#cursor.execute("INSERT INTO marca (id, nome, sigla) VALUES (1, 'Marca 1', 'M1')")
#cursor.execute("INSERT INTO veiculo (placa, ano, cor, proprietario, marca) VALUES ('ABC1234', 2022, 'Prata', 09101149350, 1)")
#banco.commit()
query = cursor.execute("SELECT * FROM pessoa;").fetchall()
print(query)
query = cursor.execute("SELECT * FROM marca;").fetchall()
print(query)
query = cursor.execute("SELECT * FROM veiculo;").fetchall()
print(query)

cursor.close()
banco.close()

import os
os.remove('database.db')