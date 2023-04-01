import sqlite3
from modelo import Pessoa, Marca, Veiculo

banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoa( nome TEXT NOT NULL, nascimento DATE NOT NULL, oculos BOOLEAN NOT NULL, cpf INTEGER PRIMARY KEY)")
#cursor.execute("CREATE TABLE marca( id INTEGER PRIMARY KEY, nome TEXT NOT NULL, sigla CHARACTER(2) NOT NULL)")
#cursor.execute("CREATE TABLE veiculo( placa CHARACTER(7) NOT NULL, ano INTEGER NOT NULL, cor TEXT NOT NULL, proprietario INTEGER NOT NULL, marca INTEGER NOT NULL, PRIMARY KEY (placa), FOREIGN KEY(proprietario) REFERENCES pessoa(cpf), FOREIGN KEY(marca) REFERENCES marca(id))")
#cursor.execute("INSERT INTO pessoa (nome, nascimento, oculos, cpf) VALUES ('Cainã', '2004-06-10', true, 09101149350)")
#cursor.execute("INSERT INTO marca (id, nome, sigla) VALUES (1, 'Marca 1', 'M1')")
#cursor.execute("INSERT INTO veiculo (placa, ano, cor, proprietario, marca) VALUES ('ABC1234', 2022, 'Prata', 09101149350, 1)")
#banco.commit()

#cursor.execute("ALTER TABLE veiculo ADD motor REAL;")

#pessoa = Pessoa(12365412390, "Paulo", "2000-01-31", True)

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?,?,?,?);'''

""" cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.usa_oculos))
banco.commit() """

""" pessoas = [
    Pessoa(12465412390, "João", "2024-01-31", True),
    Pessoa(12765412390, "Maria", "2010-01-31", True)
]

cursor.executemany(comando, [(a.cpf, a.nome, a.nascimento, a.usa_oculos) for a in pessoas])
banco.commit() """

""" pessoa = Pessoa(12865412390, "Paula", "2005-01-31", False)
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (:cpf,:nome,:nascimento,:oculos);'''
cursor.execute(comando, {"cpf": pessoa.cpf, "nome": pessoa.nome, "nascimento": pessoa.nascimento, "oculos": pessoa.usa_oculos})
banco.commit() """

""" pessoa = Pessoa(12865452390, "Pedro", "2009-01-31", False)
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (:cpf,:nome,:nascimento,:usa_oculos);'''
cursor.execute(comando, vars(pessoa))
banco.commit() """

""" comando = '''INSERT INTO marca (nome, sigla) VALUES (:nome,:sigla);'''
marcaA = Marca("Marca A", "MA")
cursor.execute(comando, vars(marcaA))
marcaA.id = cursor.lastrowid

marcaB = Marca("Marca B", "MB")
cursor.execute(comando, vars(marcaB))
marcaB.id = cursor.lastrowid
banco.commit() """

""" comando = '''UPDATE pessoa SET oculos = :usa_oculos WHERE cpf = :cpf;'''
cursor.execute(comando, {"usa_oculos": False, "cpf": 12365412390})
banco.commit() """

""" comando = '''DELETE FROM pessoa WHERE cpf = :cpf;'''
cursor.execute(comando, {"cpf": 12865452390})
banco.commit()
 """
query = cursor.execute("SELECT * FROM pessoa;").fetchall()
print(query)
query = cursor.execute("SELECT * FROM marca;").fetchall()
print(query)
query = cursor.execute("SELECT * FROM veiculo;").fetchall()
print(query)

cursor.close()
banco.close()

""" import os
os.remove('database.db') """