def depeab(n):

    div = []

    for i in range(n-1):
        if n%(i+1) == 0:
            div.append(i+1)
        else:
            continue

    for i in div:
        print(i)

    x = sum(div)

    if x < n:
        return "defeciente"
    elif x == n:
        return "perfeito"
    else:
        return "abundante"

print(depeab(6))