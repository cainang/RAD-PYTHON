txts = ["Ola, mundo!", "Ola, python", "ola!"]
with open('Aula03/texto.txt', 'w') as arquivo:
    for txt in txts:
        arquivo.write(str(txt) + '\n')


with open('Aula03/texto.txt', 'r') as arquivo:
    for linha in arquivo:
        linha_ = linha.strip()
        print(repr(linha_))

count = 0
with open('Aula03/texto.txt', 'r') as arquivo:
    for linha in arquivo:
        if linha.strip():
            count += 1
print("A quantidade de linhas é: "+ str(count))

count = 0
with open('Aula03/texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    count = texto.count("Ola")
print("A quantidade de olas é: "+ str(count))

frase = "Eu amo comer amoras no cafe da manhã"
lista = frase.split()
count = lista.count("amo")
print("A quantidade de amos é: "+ str(count))

try:
    with open("texto234.txt", "r") as arquivo:
        var_ = arquivo.read()
except FileNotFoundError as error:
    print("Arquivo inexistente")
    print("Descricao: ", error)

import os
with open("Aula03/texto234.txt", "w") as arquivo:
        arquivo.write("Relacao de disciplinas \n")
try:
    os.rename("Aula03/texto234.txt", "Aula03/texto2.txt")
except FileNotFoundError as error:
    print("Arquivo inexistente")
    print("Descricao: ", error)

with open("Aula03/texto2.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open("Aula03/texto3.txt", "w") as arquivo:
    for linha in linhas:
        _linha = linha.replace("Relacao", "", 1)
        arquivo.write(_linha)