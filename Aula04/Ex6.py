def leibnizPi4(n):
    sum = 0
    for i in range(n):
        sum = sum + ((-1)*i/(2*i+1))
    return sum



def main():
    n = int(input("N? "))
    print(leibnizPi4(n))

main()