# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>6s}{:^30s}{:<6s}".format("Numero :", "Nome", ": Morada"))
    for num in dic:
        print("{:>6s}{:^30s}{:<6s}".format(num, dic[num][0], dic[num][1]))
        # print("{:>12s} : {}".format(num, dic[num]))

# def nameToTels(partName, telList, nameList):
#     # your code here
#     lista = []
#     for i in nameList:
#         if partName in i:
#             lista.append(telList[nameList.index(i)])
#         else:
#             continue
#     return lista

# EX:
# my_dict["Address"].append("Mumbai")

def filterPartName(contacts, partName):
    dict = {}
    for num in contacts:
        if partName in contacts[num]:
            dict[contacts[num]] = num
    return dict


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("Listar (M)orada")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ["Universidade de Aveiro", "m"],
        "727392822": ["Cristiano Aveiro", "m"],
        "387719992": ["Maria Matos", "m"],
        "887555987": ["Marta Maia", "m"],
        "876111333": ["Carlos Martins", "m"],
        "433162999": ["Ana Bacalhau", "m"]
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            print("Adicionar contactos")
            num = input("Número: ")
            name = input("Nome: ")
            contactos[num] = name
        elif op == "R":
            print("Remover contactos")
            num = input("Número a remover: ")
            if num in contactos.keys():
                print(contactos[num], "removida/o!")
                contactos.pop(num)
            else:
                print("Número não existente")
        elif op == "N":
            print("Procurar número:")
            num = input("Numero: ")
            if num in contactos.keys():
                print(contactos[num], "removido/a")
                contactos.pop(num)
            else:
                print("Não encontrado")
        elif op == "P":
            print("Parte do nome:")
            pn = input("Parte do nome: ")
            print(filterPartName(contactos, pn))
        elif op == "M":
            print("Adicionar morada")
            num = input("Contacto para nova morada (numero): ")
            n2 = input("Morada: ")
            contactos[num].append(n2)

        else:
            print("Não implementado!")
    

# O programa começa aqui
main()