# mal -> objetivo: para o 2, eliminar o 2**2 , 2**3, 2**4, 2**5, etc... (while 2**x < n)
#                  para o 3, eliminar o 3**2 , 3**3, 3**4, etc (while 3**x < n)
#                  o 4 já foi eliminado no 2**2!
def primesUpTo(n):
    numbers=[]

    for i in range(n):
        numbers.append(i+1)

    nprimo = 0

    for x in numbers:
        if n%x==0:
            nprimo = nprimo + 1
        else:
            continue

    count = 0

    if nprimo == 2:
        count += 1

    return count


def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

