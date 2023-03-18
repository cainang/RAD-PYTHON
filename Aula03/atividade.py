print("Digite as notas de 5 alunos!\n\n")

notas = []
quantAlunos = 3

i = 0
while i < quantAlunos:
    nome = input("\nDigite o nome do aluno: ")
    nota = input("Digite a nota do aluno: ")

    if(nome.strip() == ""):
        print("\nNome do aluno não pode ser vazio!\n")
        continue
    
    if(nota.strip() == ""):
        print("\nNota do aluno não pode ser vazio!\n")
        continue

    lista = (nome, float(nota))
    notas.append(lista)
    i += 1

arquivo = open("Aula03/notas.txt", "w")

arquivo.write("|   Nomes   |   Notas   |")

try:
    with open('Aula03/notas.txt', 'a') as arquivo:
        for n in range(quantAlunos):
            arquivo.write("\n    " + str(notas[n][0]) + "    " + str(notas[n][1]) + "    ")
except FileNotFoundError as error:
    print("Arquivo inexistente")
    print("Descricao: ", error)
except IOError as error:
    print("Erro de permissao")
    print("Descricao: ", error)


try:
    arquivoL = open("Aula03/notas.txt", "r")

    linhas = arquivoL.readlines()

    if len(linhas) == 0:
        print("O arquivo está vazio!") 
    
    arquivoL.seek(0)
    print("\n") 
    print(arquivoL.read()) 
    arquivoL.close()

except FileNotFoundError as error:
    print("Arquivo inexistente")
    print("Descricao: ", error)
except IOError as error:
    print("Erro de permissao")
    print("Descricao: ", error)
