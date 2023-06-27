s = int(input("Segundos? "))

m = s//60

s = s%60

h = m//60

m = m%60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))