pattern = 'AAA'
dna = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']


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
        distance = distance + hamminginf
    return distance


print(distancebetweenpatternandstrings(pattern, dna))