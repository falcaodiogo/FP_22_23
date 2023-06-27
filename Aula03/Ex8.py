def intersects(a1, b1, a2, b2):
    assert a1<=b1
    assert a2<=b2
    if a2<b1:
        return True
    elif a1<b2:
        return True
    else:
        return False


def main():

    a1 = int(input("a1? "))
    b1 = int(input("b1? "))
    a2 = int(input("a2? "))
    b2 = int(input("b2? "))

    print(intersects(a1, b1, a2, b2))

main()