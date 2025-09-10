while True:
    nome = input("Insira seu nome: ")
    if len(nome) > 3:
        break
    print("Nome inválido.")

while True:
    idade = int(input("Insira sua idade: "))
    if idade > 0 or idade <= 150:
        break
    print("Idade inválida.")

while True:
    salario = float(input("Insira seu salário: "))
    if salario > 0:
        break
    print("Salário inválida.")

while True:
    sexo = input("Insira seu sexo (f ou m): ")
    if sexo == "f" or sexo == "m":
        break
    print("Sexo inválido")

while True:
    estado_civil = input("Insira seu estado civil (s, c, v, d): ")
    if estado_civil in ["s", "c", "v", "d"]:
        break
    print("Estado Civil inválido.")