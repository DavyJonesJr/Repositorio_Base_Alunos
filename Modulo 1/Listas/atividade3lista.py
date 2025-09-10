notas = []

for i in range(4):
    nota = int(input(f"Insira a {i+1}ª nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma/4

print(f"Suas notas: {notas}")
print(f"Sua média: {media}")