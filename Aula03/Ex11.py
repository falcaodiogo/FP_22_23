def countdown(n):
    assert n>=0
    print(n)
    if n==0:
        return 0
    else:
        return countdown(n-1)

def main():
    num = int(input("? "))
    countdown(num)

main()