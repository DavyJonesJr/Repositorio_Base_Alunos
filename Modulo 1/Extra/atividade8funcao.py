def contar(numero):
    quantidade = len(str(abs(numero)))
    return quantidade

numero = int(input("Insira um número: "))

print(contar(numero))