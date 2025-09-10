while True:
    a = int(input("Insira o valor da população A: "))
    b = int(input("Insira o valor da população B: "))
    if a >= b or a == 0:
        print("Insira novamente")
    else:
        break

while True:
    taxa_a = float(input("Insira o valor de taxa da população A: "))
    taxa_b = float(input("Insira o valor de taxa da população B: "))
    if taxa_a == 0 or taxa_b == 0:
        print("Insira novamente")
    else:
        break
        
anos = 0

while a < b:
    a += a * (taxa_a/100)
    b += b * (taxa_b/100)
    anos += 1

print(anos)