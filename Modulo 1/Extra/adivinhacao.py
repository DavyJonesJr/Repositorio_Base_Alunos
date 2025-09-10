import random

numero = random.randint(1, 100)
print("O computador escolheu um número entre 1 e 100")

for i in range(5):
    adivinha = int(input("Tente adivinhar qual número é: "))

    if adivinha == numero:
        print("Você ganhou")
        break
    else:
        diferenca = abs(adivinha - numero)

        if diferenca <= 10:
            if adivinha < numero:
                print("Quente! Tente um número maior")
            else:
                print("Quente! Tente um número menor")
        elif diferenca <= 30:
            if adivinha < numero:
                print("Morno! Tente um número maior")
            else:
                print("Morno! Tente um número menor")
        else:
            if adivinha < numero:
                print("Frio! Tente um número maior")
            else:
                print("Frio! Tente um número menor")

if adivinha != numero:
    print(f"Você perdeu\nO número era: {numero}")