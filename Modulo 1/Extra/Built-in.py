nome = input("Insira seu nome: ")
email = input("Insira seu email: ")

arquivo = open("pessoa.txt", "a")
arquivo.write(nome + " | " + email + "\n")
arquivo.close()

#

nome = input("Insira seu nome: ")
email = input("Insira seu email: ")

with open("pessoa.txt", "a") as arquivo:
    arquivo.write(nome + " | " + email + "\n")