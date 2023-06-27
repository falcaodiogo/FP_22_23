from numpy import double


litros = double(input("litros? "))

if litros == 0:
    print("zero")
elif litros < 0:
    print("negative")
elif litros > 0:
    if litros <= 40:
        litros=litros*1.4
    elif litros > 40:
        litros=(litros*1.4)
        litros=litros-litros*0.1
    print(litros)