def main():

    equipas = []
    nome = input("Nome equipa ")
    equipas.append(nome)
    while nome != "":
        if nome == "":
            break
        nome = input("Nome equipa ")
        equipas.append(nome)
    
    matches = allMatches(equipas)

    print(matches)

    resultados = {}

    for mat in matches:
        print(mat)
        print("------")
        print(mat[0])
        res1 = input("Resultado: ")
        print(mat[1])
        res2 = input("Resultado: ")
        resultados[mat].append((res1, res2))
    
    return resultados

def allMatches(list):
    matches = []
    if len(list) == 0:
        return []
    if len(list) == 1:
        return list
    else:
        for i in range(len(list)):
            for j in range(i+1, len(list)):
                matches.append([list[i], list[j]])
        return matches

main()