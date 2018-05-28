pattern = input("Bitte geben Sie ihren DNA-Strang ein.") #Abfrage des DNA-Stranges vom Benutzer


def patterntonumber(pattern):
    symboltonumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3} #Erstellen eines Dictionarys, Zuordnung der Buchstaben A,C,G,T zu Zahlen
    result = 0
    for k in range(len(pattern)):
        result = 4 * result + symboltonumber[pattern[k]]
    return result


print(patterntonumber(pattern))
