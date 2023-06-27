def countDigits(s):
    contador = 0
    for i in s:
        if i.isdigit() == True:
            contador += 1
        else:
            continue
    return contador

print(countDigits("23 mil 456"))