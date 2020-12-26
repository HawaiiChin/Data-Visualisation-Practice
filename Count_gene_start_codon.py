# for a given DNA string

def genestart(DNA):
    counts = 0
    for i in range(len(DNA)):
        if DNA[i:i+3] == 'ATG':
            counts = counts + 1
    return counts
