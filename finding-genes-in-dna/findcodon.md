def findcondon(dna,codon):
    dna_length = len(dna)
    codon_length = len(codon)
    codon_locations = []
    j = 0
    for i in range(0,dna_length-codon_length):
        if dna[i:i+codon_length+1)] == codon:
            j = j + 1
            codon_location.append(j)
            
