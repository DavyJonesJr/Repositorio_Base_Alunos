numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira outro número: "))
numero3 = int(input("Insira um outro número: "))

maior = numero1
menor = numero1

if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

print(f"Maior: {maior}")
print(f"Menor: {menor}")