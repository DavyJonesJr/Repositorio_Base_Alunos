tarefas = []

def adicionar_tarefa():
    nome = input("Insira o nome da tarefa: ")
    descricao = input("Insira a descrição da tarefa: ")
    tarefa = {"nome": nome,
              "descrição": descricao,
              "status": "Pendente"}
    tarefas.append(tarefa)

def exibir_tarefa():
    for tarefa in tarefas:
        print(f"{tarefa["nome"]} | Descrição: {tarefa["descrição"]} [{tarefa["status"]}]")

def completar_tarefa():
    completa = input("Insira o nome da tarefa que foi concluída: ")
    for tarefa in tarefas:
        if completa == tarefa["nome"]:
            tarefa["status"] = "Concluída"

while True:
    menu = input("1. Adicionar tarefa\n2. Exibir Tarefas\n3. Marcar tarefa como concluída\n4. Sair\nEscolha uma opção: ")
    if menu == "1":
        adicionar_tarefa()
        print("Tarefa adicionada")
    elif menu == "2":
        exibir_tarefa()
    elif menu == "3":
        completar_tarefa()
        print("Tarefa completa")
    elif menu == "4":
        print("Raleu viu mofi! Raleu")
        break
    else:
        print("Valor inválido")