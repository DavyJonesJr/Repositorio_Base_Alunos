def somaImposto(taxaImposto, custo):
    soma = custo * (taxaImposto/100)
    custo_final = soma + custo
    return custo_final

taxaImposto = float(input("Insira a taxa do imposto: "))
custo = float(input("Insira o custo do item: "))

print(somaImposto(taxaImposto, custo))