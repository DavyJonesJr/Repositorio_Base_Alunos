def calcular(numero1, numero2):
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        resultado = numero1 / numero2
    else:
        resultado = "Operação inválida."

    return resultado

operacao = input("Insira a operação a ser realizada (+, -, *, /): ")
numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira outro número: "))

print(calcular(numero1, numero2))