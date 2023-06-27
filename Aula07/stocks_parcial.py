
# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[1])
    print("last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    cont = 0
    while cont != 220:
        for tupl in lst:
            cont += 1
            totVol[tupl[NAME]] = tupl[VOLUME]
    return totVol

def maxValorization(lst):
    vMax = {}
    # O ficheiro tem dados realativos aos mesmos dias para diferentes empresas
    cont = 0
    val = 0
    while cont != 220:
        for tupl in lst:
            cont += 1
            if val > tupl[CLOSE]/tupl[OPEN]-100:
                val = (tupl[CLOSE]/tupl[OPEN])
                vMax[tupl[NAME]] = val
            else:
                continue


    return vMax

def stocksByDateByName(lst):
    stocks = {}
    for tupl in lst:
        if tupl[DATE] not in stocks:
            stocks[tupl[DATE]] = {}
        stocks[tupl[DATE]][tupl[NAME]] = tupl
    return stocks

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for stock in portfolio:
        val += portfolio[stock] * stocks[date][stock][CLOSE]
    return val

if __name__ == "__main__":
    main()
