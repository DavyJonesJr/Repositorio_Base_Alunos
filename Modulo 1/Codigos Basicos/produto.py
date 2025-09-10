nome_produto = input("Insira o nome do produto: ")
valor_produto = float(input("Insira o valor do produto: "))
desconto_produto = int(input("Insira o desconto do produto: "))

preco_desconto = valor_produto * (desconto_produto/100)
preco_final = valor_produto - preco_desconto

print(f"Nome do produto: {nome_produto}. Preço final: {preco_final}")