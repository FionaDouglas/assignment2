import random


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
    prefixpattern = numbertopattern(prefixindex, k - 1)
    return prefixpattern + symbol


symboltonumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def patterntonumber(text):
    result = 0
    for k in range(len(text)):
        result = 4 * result + symboltonumber[text[k]]
    return result


def profileprobable(text, k, profile):
    maxprob = 0
    kmer = text[0:k]
    for i in range(0, len(text) - k + 1):
        prob = 1
        pattern = text[i:i + k]
        for j in range(k):
            l = symboltonumber[pattern[j]]
            prob *= profile[l][j]
        if maxprob < prob:
            maxprob = prob
            kmer = pattern
    return kmer


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
        hamminginf = k + 1
        for i in range(len(subpattern) - k + 1):
            if hamminginf > hammingdistance(pattern, subpattern[i:i + k]):
                hamminginf = hammingdistance(pattern, subpattern[i:i + k])
        distance += hamminginf
    return distance


def profileform(motifs):
    k = len(motifs[0])
    profile = [[1 for i in range(k)] for j in range(4)]
    for x in motifs:
        for i in range(len(x)):
            j = symboltonumber[x[i]]
            profile[j][i] += 1
    for x in profile:
        for i in range(len(x)):
            x[i] = x[i] / len(motifs)
    return profile


def consensus(profile):
    str = ""
    for i in range(len(profile[0])):
        max = 0
        loc = 0
        for j in range(4):
            if profile[j][i] > max:
                loc = j
                max = profile[j][i]
        str += numbertosymbol(loc)
    return str


def score(motifs):
    profile = profileform(motifs)
    cons = consensus(profile)
    score = 0
    for x in motifs:
        for i in range(len(x)):
            if cons[i] != x[i]:
                score += 1
    return score


def randomizedmotifsearch(dna, k, t):
    motifs = []
    bestmotifs = []
    for x in range(0, t):
        random.seed()
        i = random.randint(0, len(dna[x])-k)
        motifs.append(dna[x][i:i+k])
    bestmotifs = motifs.copy()
    count = 0
    while True:
        profile = profileform(motifs)
        for x in range(t):
            motifs[x] = profileprobable(dna[x], k, profile)
        if score(bestmotifs) > score(motifs):
            bestmotifs = motifs.copy()
            count += 1
        else:
            print(count)
        return bestmotifs


#Defintion der festgelegten Eingaben:

dna = [
    "ACTTATATCTAGAGTAAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGA"
    "TTTCTGGCACTAACTACCCAAAATCGAGTGATTGAACTGACTTATATCTAGAGT",
    "ACAAGAACTGGTGGGGAGACTATGACACTCTAGCGGTCGCATAAGGGCCGGAAACCAGGACAAATCGATAAGATGAAGCGGGGATATAAGCCTTATACTGCGACTGGTTCCTTA"
    "TATTATTTAGCCCCGATTGATCACCGATTAAAATATTCTGCGGTTTTCGAGACGG",
    "TAACCACACCTAAAATTTTTCTTGGTGAGATGGACCCCCGCCGTAAATATCAGGATTAAATGTACGGATACCCATGACCCTCCAGTCATCTACCTTCCCGTGGTGGTCGCTCAGC"
    "CTTGTGCAGACCGAACTAGCACCTGTCACATACAATGTTGCCCGCATAGATCGT",
    "ATCCGACAGAGGCAGTGAATAAGGTTTCGTTTCCTCAGAGAGTAGAACTGCGTGTGACCTTGCCTTCACCGACATCCGTTTCCAATTGAGCTTTTCAGGACGTTTAGGTAACTGA"
    "TTGTCATTGCAATTGTCCGGGGGATTTAGATGGCCGGGTACCTCTCGGACTATA",
    "CCTTGTTGCCACCGATTCGCGAGCAACATCGGAGTGCTCTGATTCACGGCGATGCTCCACGAAGAGGACCGCGGCACGACACGCCCTGTACCTACGTTTCTGGATATCCTCCGGC"
    "GAGTTAATAGAGCAATACGACCTGGTCGTCGAGATCGTGTATCTAGCCCTACCT",
    "ATAGGTTAACGAATCAGGAGAGTTAATTTTACCTAGCTAGAGCGGACGGTGCCTGGCTGTATTCGCGTTTGACTTTCGGGCTCGCTGATAACTTGTGATCACCTTTTACGCTTAC"
    "TGGATCCAACGATGGATCAAAGTTGAGAATTTCTGTGCCTTGGGTGTGAGCTGT",
    "CTGACGAAAGGACGGGCGGTGTACTTAGTTTGGGGTAAAATAGTTGGTATAATTCTGTGCGACAGACATTTGGTCAGGCCATACTGCCATATCGTGATGTAACTATCCACACTAC"
    "GTCATAGGCCCTTGTGATCAATTAAACGTTCCTCATGCCAGGCTATCTGTTTAA",
    "GGCTTCGCGTTTAAGGCTGGATTAAGTACTCCGCCTTGTGATCTGTGATCCTCCGACCTGTGATCAGCAAGATTGGAACCTAGGTAGGCGGCGGGTCTACGCTGGCCCACAATCG"
    "TGAGTCCCCCACTCCGTAGGTTGTGGAATTTATAGACCCGCAAGGGGCACCACT",
    "AGGATGACACCCAGGATGAATCTGGATTAGGAACACCAACCCGACATATTTGTTACCGCTGCAGCATTTCGCTCTTGGACGCGTAACCCGAGATCCGTCTCGCGATCGTCACGGA"
    "TCGGGATTATGCAGGCAATACCTTGTGATCACTCCGCGCTTGGTTTTGCTAGCG",
    "ACATCTCTAGTCACTTTTATTGAGCAGGTGGGCGGATTCATGATCCGGCTCTGTCGTACGTCCAACCACGGTGACATGTTCGGAGCTGTCGCCGTGGAGCAGAGATACATCGGAT"
    "CTATCAATTTTACTAAGAGCAACTAGCCACGACAAACTGTGATCACCGATTGGA",
    "AATTTGCGTATCTCTAGGACTCCCTCATACAAATCAAAGCTTGGATGGGTAAGATGCCGCAGCAGCAGGTATCTCATATTGGCTATTAAGAGCCAGGCCCTATGGCCTTAGTATC"
    "ACCGATCAGACGTCGCATGAGCGGGCCCGTTGTCCTATCTCTTTAGCTGCCGCA",
    "GAAGTAAAGGGGTTCCACTGCGTAGAGCGTGCCCCTCTGGTGTGCCGTACTGTTATGGTGATACAGCTTCCTTATACCCCTCGTAAAGCGGCTAATGGTCCTAATGAATGCCCTT"
    "GTGAAATCCGAATCGCTTTACAATTGCGTTCGGCGGAATGCAGTCACCAGTGTT",
    "TACACTACGCGTTATTTACTTTTACTGAGTCCTTGTCGCCACCGAACGAGGATTGTTCATTGTATCCGGAGATTAGGAGTTCGCATCGCTGACACAGCCAGTTCGTAGCAAATAC"
    "CGCTGGCCCTGGGCACTCCAGATCAGAACTACTAGCCCTAAACTCTATGACACA",
    "TTGGGTCTCGATCCCTCTATGTTAAGCTGTTCCGTGGAGAATCTCCTGGGTTTTATGATTTGAATGACGAGAATTGGGAAGTCGGGATGTTGTGATCACCGCCGTTCGCTTTCAT"
    "AAATGAACCCCTTTTTTTCAGCAGACGGTGGCCTTTCCCTTTCATCATTATACA",
    "TTTCAAGTTACTACCGCCCTCTAGCGATAGAACTGAGGCAAATCATACACCGTGATCACCGACCCATGGAGTTTGACTCAGATTTACACTTTTAGGGGAACATGTTTGTCGGTCA"
    "GAGGTGTCAATTATTAGCAGATATCCCCCAACGCAGCGAGAGAGCACGGAGTGA",
    "GATCCATTACCCTACGATATGTATATAGCGCCCTAGTACGGCTTCTCCCTTGCAGACACGCAGGCGCTGTGCGCTATCGGCTTCCTCGGACATTCCTGGATATAAGTAACGGCGA"
    "ACTGGCTATCACTACCGCCGCTCCTTAAGCCTTGGTTTCACCGACGATTGTCGT",
    "TAGTAGATTATTACCTGTGGACCGTTAGCTTCAAGACCGAAACGTTGGTGATGCTACTTAAATGTCAAGAGTTGCGAAGTTGGGCGAAGCACATCCGTACTCCCAAGTGGACGAT"
    "CGATAGATCCATGGAGTTTCCATCCATCTTAATCCGCCCTTTGCATCACCGACG",
    "TACAAGGCACAAACGAGACCTGATCGAACGGTGCACGGTCGAGGCAGCGAGATAAATGTACATTGAGAGCACCTTGTGATTTACGACCTGCATCGAAGGTTTCTTGGCACCCAC"
    "CTGTCGTCCGCCAGGGCAGAGCCGACATTATATGACGCTGATGTACGAAGCCCCT"]
k = 20
t = 15

best = randomizedmotifsearch(dna, k, t)
min = score(best)


#Der Algorithmus soll 1000 mal laufen:

for x in range(1000):
    print(x)
    y = randomizedmotifsearch(dna, k, t)
    if score(best) > score(y):
        best = y
        min = score(y)
print(min)
for x in best:
    print(x)
