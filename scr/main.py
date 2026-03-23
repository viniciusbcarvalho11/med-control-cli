from scr.medication import Medication

medications = []

def add_medication():
    name = input("Nome do medicamento: ")
    time = input("Horário (HH:MM): ")

    if not name or not time:
        print("Entrada inválida!")
        return

    med = Medication(name, time)
    medications.append(med)
    print("Medicamento adicionado!")

def list_medications():
    if not medications:
        print("Nenhum medicamento cadastrado.")
        return

    for i, med in enumerate(medications):
        print(f"{i} - {med}")

def mark_taken():
    list_medications()
    try:
        index = int(input("Digite o índice: "))
        medications[index].mark_as_taken()
        print("Marcado como tomado!")
    except:
        print("Erro!")

def menu():
    while True:
        print("\n1. Adicionar")
        print("2. Listar")
        print("3. Marcar como tomado")
        print("4. Sair")

        option = input("Escolha: ")

        if option == "1":
            add_medication()
        elif option == "2":
            list_medications()
        elif option == "3":
            mark_taken()
        elif option == "4":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()