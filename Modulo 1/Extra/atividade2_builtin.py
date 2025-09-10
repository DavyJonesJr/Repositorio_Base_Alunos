nome = input("Insira o nome do produto: ")
valor = float(input("Insira o valor do produto: "))
quantidade = int(input("Insira a quantidade do produto: "))

with open("produtos.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome} | Valor: {valor} | Quantidade: {quantidade} \n")