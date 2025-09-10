nome = input("Insira seu nome: ")
peso = int(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / (altura **2)

def calculo(nome, peso, altura):
    if imc < 18.5:
        resultado = "Abaixo do peso"
    elif imc <= 24.9:
        resultado = "Peso normal"
    elif imc <= 29.9:
        resultado = "Sobrepeso"
    elif imc <= 34.9:
        resultado = "Obesidade Grau I"
    elif imc <= 39.9:
        resultado = "Obesidade Grau II"
    else:
        resultado = "Obesidade Grau III"
    return resultado


with open("imc.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome} | IMC: {imc} | {calculo(nome, peso, altura)}\n")