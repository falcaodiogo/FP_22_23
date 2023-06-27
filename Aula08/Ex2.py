nomes = dict()

with open ('names.txt', 'r') as file:
    file.readline()
    for linha in file:
        lista = linha.split(" ")
        a = lista[-1].strip()
        if a not in nomes:
            nomes[a] = set()
        nomes[a].add(lista[0])

for k, v in nomes.items():
    print(k, ":", v)