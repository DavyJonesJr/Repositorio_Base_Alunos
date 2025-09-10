nomes = ["Boboa", "Cacatua", "Marley"]
nomes.append("Ronaldo")
nomes.insert(1, "Snake")
nomes[2] = "Hugo Chaves"
del nomes[3]
nomes.remove("Boboa")
removido = nomes.pop()
nomes.clear()
print(removido, nomes)

