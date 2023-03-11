arquivo = open("Aula02/texto.txt")

print(arquivo)
print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)
print(arquivo.read())
print(arquivo.seek(0))
print(arquivo.read()) 
print(arquivo.tell()) 
print(arquivo.seek(0))
print(arquivo.readline()) 
print(arquivo.seek(0))
print(arquivo.readlines()) 
arquivo.close()
print(arquivo.closed) 

arquivo2 = open("Aula02/texto2.txt", "w")
print(arquivo)

precos = [200, 100, 500, 600]

with open('Aula02/texto2.txt', 'w') as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')

precos = [1000]
with open('Aula02/texto2.txt', 'a') as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')

arquivo = open('Aula02/texto2.txt', 'r')

tipos = arquivo.readlines()
tipos.append('Nova linha \n')

arquivo = open('Aula02/texto3.txt', 'w')
arquivo.writelines(tipos)
arquivo.close()