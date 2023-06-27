tempoinicial = 6*60*60+52*60
umkm = 60*10
doikm = 6*3*60
segundos = tempoinicial + umkm + doikm
minutos = segundos // 60
segundos = segundos % 60
horas = minutos // 60
minutos = minutos%60

print("{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))