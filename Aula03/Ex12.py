def mdc(a, b):
    if b==0:
        return a
    else:
        return mdc(b, a%b)

def main():
    num1 = int(input("Num1? "))
    num2 = int(input("Num2?"))
    print(num1, num2)

main()