list = [1+2*5, 17/3.0, 17/3, 17//3, 17%3.0, 5.0/0.75, 5.0//0.75, 'error', 'tau'+'rus',  'tau'*2]

def tabela(x):
    contador = 1
    for x in list:
        print(contador, ": ", x, " tipo: ", type(x))
        contador=contador+1

tabela(list)