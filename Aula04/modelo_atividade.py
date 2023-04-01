class Alunos:
    def __init__(self, cpf, nome, nascimento):
        self.cpf = cpf
        self.nome = nome 
        self.nascimento = nascimento
    
class Disciplina:
    def __init__(self, id, nome, professor):
        self.id = id
        self.nome = nome
        self.professor = professor

class Notas:
    def __init__(self, id, nota_1, nota_2, nota_3, aluno_id, disciplina_id):
        self.id = id
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.aluno_id = aluno_id
        self.disciplina_id = disciplina_id