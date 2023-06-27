andares = int(input("Andares? "))
moradores = int(input("Moradores? "))
km = 0

for i in range(andares):
    km += andares*i*365

print ("A distância percorrida é de ", km, "km")

metros = km * 1000  

segundos = metros

minutos = segundos // 60

segundos = segundos % 60

horas = minutos // 60

print("{:02d} horas".format(horas))