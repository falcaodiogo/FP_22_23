# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, 'r') as file:
        file.readline()
        for line in file:
            s = ()
            nwlt = tuple(line.split('\t'))
            s += (nwlt[0]) + (nwlt[1]) + (nwlt[5]) + (nwlt[6]) + (nwlt[7])
        lst.append(s)
    return lst

    
# b) Crie a função notaFinal aqui...
def notaFnal(reg):
    return ((float(reg(5)) + float(reg(6)) + float(reg(7))) / 3)


# c) Crie a função printPauta aqui...
def printPauta(lst, file):
    with open(file, 'w') as doc:
        doc.write("{:<8} {:^15} {:>8}".format('Pos','Lang','Percent'))
        for tpl in lst:
            doc.write("{:<8} {:^15} {:>8}".format(tpl(1), tpl(0), notaFnal(lst)))


# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort(key=lambda x: x[0])

    # imprimir a pauta
    printPauta(lst)

# Call main function
if __name__ == "__main__":
    main()


