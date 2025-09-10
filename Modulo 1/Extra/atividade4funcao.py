def retorno():
    if argumento <= 0:
        valor = "Negativo"
    else:
        valor = "Positivo"
    return valor

argumento = int(input("Insira um número: "))

print(retorno())