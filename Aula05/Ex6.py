def shorten(s):
    string = ""
    for i in s:
        if i.isupper() == True:
            string += i
        else:
            continue
    return string

print(shorten("Universidade de Aveiro"))