def hms2sec(sec):
    h, m, s = sec//3600, (sec%3600)//60, (sec%3600)%60
    return h, m, s

def main():
    sec = int(input("Segundos? "))
    print(hms2sec(sec))

main()