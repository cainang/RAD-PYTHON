import sqlite3
from modelo_atividade import Alunos, Disciplina, Notas

banco = sqlite3.connect('database_atividade.db')
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()

cursor.execute("CREATE TABLE alunos( nome TEXT NOT NULL, nascimento DATE NOT NULL, cpf INTEGER PRIMARY KEY)")
cursor.execute("CREATE TABLE disciplinas( id INTEGER PRIMARY KEY, nome TEXT NOT NULL, professor TEXT NOT NULL)")
cursor.execute("CREATE TABLE notas(  id INTEGER, nota_1 DOUBLE NOT NULL, nota_2 DOUBLE NOT NULL, nota_3 DOUBLE NOT NULL, aluno_id INTEGER NOT NULL, disciplina_id INTEGER NOT NULL, PRIMARY KEY (id), FOREIGN KEY(aluno_id) REFERENCES alunos(cpf), FOREIGN KEY(disciplina_id) REFERENCES disciplinas(id))")
#cursor.execute("INSERT INTO pessoa (nome, nascimento, oculos, cpf) VALUES ('Cainã', '2004-06-10', true, 09101149350)")
#cursor.execute("INSERT INTO marca (id, nome, sigla) VALUES (1, 'Marca 1', 'M1')")
#cursor.execute("INSERT INTO veiculo (placa, ano, cor, proprietario, marca) VALUES ('ABC1234', 2022, 'Prata', 09101149350, 1)")
#banco.commit()

comando = '''INSERT INTO alunos (nome, nascimento, cpf) VALUES (:nome,:nascimento,:cpf);'''

aluno1 = Alunos(12345678901, "Aluno 01", "2022-01-01")
cursor.execute(comando, vars(aluno1))

aluno2 = Alunos(12345978901, "Aluno 02", "2026-01-01")
cursor.execute(comando, vars(aluno2))

comando = '''INSERT INTO disciplinas (id, nome, professor) VALUES (:id,:nome,:professor);'''

disciplina = Disciplina(1, "Portugues", "Fulano")
cursor.execute(comando, vars(disciplina))

comando = '''INSERT INTO notas (id, nota_1, nota_2, nota_3, aluno_id, disciplina_id) VALUES (:id, :nota_1, :nota_2, :nota_3, :aluno_id, :disciplina_id);'''

nota1 = Notas(1, 10.0, 5.0, 8.0, aluno1.cpf, disciplina.id)
cursor.execute(comando, vars(nota1))

nota2 = Notas(2, 4.0, 7.0, 4.0, aluno2.cpf, disciplina.id)
cursor.execute(comando, vars(nota2))

comando = '''UPDATE notas SET nota_1 = :nota_1 WHERE id = :id;'''
cursor.execute(comando, {"nota_1": 6.0, "id": nota1.id})
cursor.execute(comando, {"nota_1": 9.0, "id": nota2.id})

banco.commit()

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