import sqlite3

banco = sqlite3.connect('database_atividade.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE alunos( nome TEXT NOT NULL, nascimento DATE NOT NULL, cpf INTEGER PRIMARY KEY)")
cursor.execute("CREATE TABLE disciplinas( id INTEGER PRIMARY KEY, nome TEXT NOT NULL, professor TEXT NOT NULL)")
cursor.execute("CREATE TABLE notas(  id INTEGER, nota_1 DOUBLE NOT NULL, nota_2 DOUBLE NOT NULL, nota_3 DOUBLE NOT NULL, aluno_id INTEGER NOT NULL, disciplina_id INTEGER NOT NULL, PRIMARY KEY (id), FOREIGN KEY(aluno_id) REFERENCES alunos(id), FOREIGN KEY(disciplina_id) REFERENCES disciplinas(id))")
#cursor.execute("INSERT INTO pessoa (nome, nascimento, oculos, cpf) VALUES ('Cainã', '2004-06-10', true, 09101149350)")
#cursor.execute("INSERT INTO marca (id, nome, sigla) VALUES (1, 'Marca 1', 'M1')")
#cursor.execute("INSERT INTO veiculo (placa, ano, cor, proprietario, marca) VALUES ('ABC1234', 2022, 'Prata', 09101149350, 1)")
#banco.commit()
query = cursor.execute("SELECT * FROM alunos;").fetchall()
print(query)
query = cursor.execute("SELECT * FROM disciplinas;").fetchall()
print(query)
query = cursor.execute("SELECT * FROM notas;").fetchall()
print(query)

cursor.close()
banco.close()

#import os
#os.remove('database_atividade.db')