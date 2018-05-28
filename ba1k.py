text = input("Bitte geben Sie den DNA Strang ein.")  # Abfrage des DNA-Stranges vom Benutzer
k = int(input("Bitte geben Sie die Länge des k-mers ein."))  # Abfrage der Länge des k-mers vom Benutzer

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


print(frequencyarray(text, k))
