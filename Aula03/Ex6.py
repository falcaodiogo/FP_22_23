def max(x1, x2, x3):
    if x1 > x2 and x1 > x3:
        return(x1)
    elif x2 > x1 and x2 > x3:
        return(x2)
    elif x3 > x1 and x3 > x2:
        return(x3)
    else:
        return(x1, " ou ", x2, " ou ", x3)

print(max(1, 2, 3))