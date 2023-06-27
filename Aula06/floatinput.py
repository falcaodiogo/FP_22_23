import math

def floatInput(prompt):
    res = float(input(prompt))
    return res


def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    try:
        v = floatInput("Value? ")
        print(v)
    except ValueError:
        print("Not a float")
        v = floatInput("Value? ")
        print(v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    try:
        h = floatInput("Value? ")
        if h>= 0 and h<=100:
            print(h)
        else:
            print("Not in [0, 100]")
            h = floatInput("Value? ")
            print(h)
    except ValueError:
        print("Not a float")
        h = floatInput("Value? ")
        if h>= 0 and h<=100:
            print(h)
        else:
            print("Not in [0, 100]")
            h = floatInput("Value? ")
            print(h)

    print("c) Try entering invalid values such as 23C or -274.")
    op = input("Do you want not min and/or max? Write m, M, or mM")
    if op == "m":
        print("Not min selected")
        try:
            t = floatInput("Temperature (Celsius)? ")
            if t<=100:
                print(t)
            else:
                print("Not in [inf, 100]")
                t = floatInput("Value? ")
                print(t)
        except ValueError:
            print("Not a float")
            t = floatInput("Value? ")
            if t<=100:
                print(t)
            else:
                print("Not in [inf, 100]")
                t = floatInput("Value? ")
                print(t)
    elif op == "M":
        print("Not Max selected")
        try:
            t = floatInput("Temperature (Celsius)? ")
            if t>= 0:
                print(t)
            else:
                print("Not in [0, inf]")
                t = floatInput("Value? ")
                print(t)
        except ValueError:
            print("Not a float")
            t = floatInput("Value? ")
            if t>= 0:
                print(t)
            else:
                print("Not in [0, inf]")
                t = floatInput("Value? ")
                print(t)
    elif op == "mM":
        print("None selected")
        try:
            v = floatInput("Value? ")
            print(v)
        except ValueError:
            print("Not a float")
            v = floatInput("Value? ")
            print(v)
    else:
        print("None selected")
        try:
            v = floatInput("Value? ")
            print(v)
        except ValueError:
            print("Not a float")
            v = floatInput("Value? ")
            print(v)




    # d) What happens if you uncomment this?
    # impossible = floatInput("Value in [3, 0]? ", min=3, max=0)

    return

if __name__ == "__main__":
    main()
