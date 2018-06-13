dna = ['AAATTGACGCAT', 'GACGACCACGTT','CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
k = 3


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


def hammingdistance(dnastring1, dnastring2):
    mismatches = 0
    for i in range(len(dnastring1)):
        if dnastring1[i] != dnastring2[i]:
            mismatches += 1
    return mismatches


def distancebetweenpatternandstrings(pattern, dna):
    distance = 0
    k = len(pattern)
    for subpattern in dna:
        hamminginf = k+1
        for i in range(len(subpattern)-k+1):
            if hamminginf > hammingdistance(pattern, subpattern[i:i+k]):
                hamminginf = hammingdistance(pattern, subpattern[i:i+k])
        distance += hamminginf
    return distance


def medianstring(dna, k):
    median = ""
    distance = (k+1) * len(dna)
    for i in range(0, ((4**k)-1)):
        pattern = numbertopattern(i, k)
        x = distancebetweenpatternandstrings(pattern, dna)
        if distance > x:
            distance = x
            median = pattern
    return median


print(medianstring(dna, k))
