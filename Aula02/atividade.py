print("Digite as notas de 5 alunos!/n/n")

notas = []
quantAlunos = 3

for n in range(quantAlunos):
    nome = input("\nDigite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    lista = (nome, nota)
    notas.append(lista)

arquivo = open("Aula02/notas.txt", "w")

arquivo.write("|   Nomes   |   Notas   |")

with open('Aula02/notas.txt', 'a') as arquivo:
    for n in range(quantAlunos):
        arquivo.write("\n    " + str(notas[n][0]) + "    " + str(notas[n][1]) + "    ")

arquivo = open("Aula02/notas.txt", "r")

print(arquivo.read()) 

arquivo.close()