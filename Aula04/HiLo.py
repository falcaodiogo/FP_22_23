#Não pode criar, editar nem carregar conteúdo … Sem armazenamento suficiente. Obtenha já mais armazenamento ou remova ficheiros do Drive, Google Fotos ou Gmail.
# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)
    contador = 0
    print("Can you guess my secret?")
    # put your code here
    tentativa = int(input("Tentativa? "))
    while tentativa != secret:
        if tentativa < secret:
            print("Muito baixo!")
            tentativa = int(input("Tentativa? "))
        else:
            print("Muito alto!")
            tentativa = int(input("Tentativa? "))
        contador +=1
    print("CERTO em {} tentativas".format(contador))


main()