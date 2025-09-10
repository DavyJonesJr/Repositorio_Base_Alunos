nome = input("Insira seu nome: ")
peso = int(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / (altura **2)

print(f"Nome do paciente: {nome}")
print(f"Valor do imc: {imc}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade Grau I")
elif imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")