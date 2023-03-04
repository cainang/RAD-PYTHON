print("hello world")

soma = 1 + 1

print(soma)

frase = "Python para ánalise de dados"
print(frase[0:10])
print(frase.count("pandas"))
print(frase.count("Python"))
print(frase.lower())
print(frase.upper())
print(frase.capitalize())

lista = [1,"String",3.2]

print(lista)
print(lista[1])

lista[1] = "Papagaio"

print(lista)

lista.insert(1, "Gato")

print(lista)

lista.remove("Gato")

print(lista)

print("Papagaio" in lista)
print("Gato" in lista)

lista.append("Cobra")

print(lista)

listas = [[0,"Cachorro"], [2,3]]

print(listas)

print(listas[0][1])
print(listas[1][1])

tp = ("Banana", "Maçã", 10, 10.5)
print(tp)
print(tp[1])
print(type(tp))

dc = {"Maçã": 20, "Banana": 10, "Laranja": 15, "Uva": 5}

print(dc)
print(dc["Maçã"])

print(10 == 20)

nome = "Cainã"
if 10 > 20 or nome == "Cainã":
    print("Olá " + nome + ", seja bem vindo(a)!")
else:
    print("Você não é " + nome)

for i in ["Fusca", "Ferrari", "Audi"]:
    print(i)

def imc(peso, altura):
    return peso/(altura**2)

print(imc(57, 1.70))