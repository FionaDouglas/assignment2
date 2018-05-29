def patterntonumber(text):
    symboltonumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3} #Erstellen eines Dictionarys, Zuordnung der Buchstaben A,C,G,T zu Zahlen
    result = 0
    for k in range(len(text)):
        result = 4 * result + symboltonumber[text[k]]
    return result


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


def patterntonumber(text):
    symboltonumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}  # Erstellen eines Dictionarys, Zuordnung der Buchstaben zu Zahlen
    result = 0
    for k in range(len(text)):
        result = 4 * result + symboltonumber[text[k]]
    return result


def frequencyarray(text, k):
    array = [0] * (4 ** k)
    for i in range(0, (len(text) - k + 1)):
        pattern = text[i: i + k]
        j = patterntonumber(pattern)
        array[j] = array[j] + 1

    return array


from collections import Counter

def counter():
    words = []
    results = []
    string = input("Bitte geben Sie ihren DNA-Strang ein.") #Abfrage des DNA-Stranges vom Benutzer
    k = int(input("Bitte geben Sie die Länge des k-mers ein. ")) #Abfrage der Länge des k-mers vom Benutzer

    for i in range(len(string)):
        words.append("".join(string[i: i+k]))
        tuples = Counter(words).most_common()
        max_count = max([y for (x, y)in tuples])

    for (x,y) in tuples:
        if y == max_count:
            results.append(x)
    return results

print (counter()) #Ausgabe der am häufigsten vorkommenden k-mere
