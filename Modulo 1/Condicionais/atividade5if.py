nota1 = float(input("Insira uma nota: "))
nota2 = float(input("Insira outra nota: "))

media = (nota1 + nota2) / 2

print(media)

if media >= 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")