produto1 = int(input("Insira o valor do 1º produto: "))
produto2 = int(input("Insira o valor do 2º produto: "))
produto3 = int(input("Insira o valor do 3º produto: "))

menor = produto1

if produto2 < menor:
    menor = produto2
if produto3 < menor:
    menor = produto3

print(f"Você devo comprar o produto que custa: {menor}")