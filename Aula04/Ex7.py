def media(num):
    contador = 1
    while num != "":
        num2 = (input("NUM? "))
        if num2 == "":
            break
        else:
            num = int(num) + int(num2)
            contador += 1
            num = num2
    print("Média: ", int(num)/contador)

def main():
    num = input("NUM? ")
    media(num)

main()