def isPrime(n):

    numbers=[]
    for i in range(n):
        numbers.append(i+1)

    nprimo = 0

    for x in numbers:
        if n%x==0:
            nprimo = nprimo + 1
        else:
            continue

    if nprimo == 2:
        return "primo"
    else:
        return "não primo"

print(isPrime(8))