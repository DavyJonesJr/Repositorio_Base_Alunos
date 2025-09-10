lista = []
repetidor = 0

while repetidor <= 9:
    numero = int(input("Insira um número: "))
    lista.append(numero)
    repetidor += 1

inverso = lista[::-1]
print(inverso)