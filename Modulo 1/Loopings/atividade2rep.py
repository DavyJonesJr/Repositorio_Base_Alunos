while True:
    nome = (input("Nome do usuário: "))
    senha = (input("Senha: "))
    if nome != senha:
        break
    print("A senha e o nome não podem ser iguais. Insira novamente.")