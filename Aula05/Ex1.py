def inputFloatList():

    floatlist = []

    while True:
        try:
            floatlist.append(float(input("Digite um número: ")))
        except ValueError:
            break
    
    return floatlist


def countLower(lst, v):

    count = 0

    for i in lst:
        if i < v:
            count += 1

    return count

def countHigher(lst, v):

    count = 0

    for i in lst:
        if i > v:
            count += 1

    return count

def minmax(lst):

    min = lst[0]
    max = lst[0]

    for i in lst:
        if i < min:
            min = i
        if i > max:
            max = i

    return min, max

def main():
    
        lst = inputFloatList()
    
        print("Menor valor: ", minmax(lst)[0])
        print("Maior valor: ", minmax(lst)[1])
        print("Quantidade de valores menores que 10: ", countLower(lst, 10))
        print("Quantidade de valores maiores que 10: ", countHigher(lst, 10))

main()