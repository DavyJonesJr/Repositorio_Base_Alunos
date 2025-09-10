notas = []
repetidor = 0

while repetidor <= 3:
    nota = float(input(f"Insira a nota: "))
    notas.append(nota)
    repetidor += 1

media = sum(notas) / 4

print(media)