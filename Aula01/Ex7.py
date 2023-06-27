primeiro = 3*2*365
segundo = 6*2*365
terceiro = 9*2*365

km = primeiro + segundo + terceiro

print ("A distância percorrida é de ", km, "km")

metros = km * 1000  

segundos = metros

minutos = segundos // 60

segundos = segundos % 60

horas = minutos // 60

#não dá certo(?)
print("{:02d} horas".format(horas))