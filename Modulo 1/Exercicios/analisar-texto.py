texto = input("Insira ou cole um texto aqui: ")

palavras = texto.split()
vogais = "aeiouAEIOU"
consoantes ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

maior_palavra = max(palavras, key=len)

quantidade_vogais = 0
quantidade_consoantes = 0

for letra in texto:
    if letra in vogais:
        quantidade_vogais += 1
    elif letra in consoantes:
        quantidade_consoantes += 1

print(f"Total de palavras: {len(palavras)}")
print(f"Palavra mais longa: {maior_palavra}")
print(f"Vogais: {quantidade_vogais} | Consoantes: {quantidade_consoantes}")