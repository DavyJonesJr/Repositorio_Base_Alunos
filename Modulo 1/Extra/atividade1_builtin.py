aluno = input("Insira o nome do aluno: ")

notas = []

for i in range(4):
    nota = int(input(f"Insira a {i+1}ª nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma/4

with open("aluno_media.txt", "a") as dados:
    dados.write(f"Aluno: {aluno} | Notas: {notas} | Media: {media}\n")