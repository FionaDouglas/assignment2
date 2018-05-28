index = int(input("Bitte geben Sie eine Zahl ein.")) #Abfrage des Index vom Benutzer
k = int(input("Bitte geben Sie die Länge des k-mers ein.")) #Abfrage der Länge des k-mers vom Benutzer


def numbertosymbol(index):
    if index == 0:
        return 'A'
    if index == 1:
        return 'C'
    if index == 2:
        return 'G'
    if index == 3:
        return 'T'


def numbertopattern(index, k):
    if k == 1:
        return numbertosymbol(index)

    prefixindex = index // 4
    n = index % 4
    symbol = numbertosymbol(n)
    prefixpattern = numbertopattern(prefixindex, k-1)

    return prefixpattern + symbol


print(numbertopattern(index, k))  #Ausgabe des k-mers

