# Author: Cyrille NJUME
# Version 05.07.2021

def findStartCodon(dna, start_location):
    """
    dna: a string of ATGC characters representing the nucleotides of a DNA molecule
    start_location: an integer, index on the dna string where the start codon search should begin
    startIndex: output of the function. Also the index of the found start codon. If no start codon is found, startIndex is given a None value
    """
    dna = dna.upper()       # ensuring that all letters of the dna string are uppercase.
    startCodon = "ATG"      # "ATG" is the start codon for every gene in mammals
    dna_length = len(dna)
    startIndex = None
    for i in range(start_location,dna_length-3): #  slicing through the dna string to see if any substring matches with the start codon
        if dna[i:i+3] == startCodon:
            startIndex = i
            break
    return startIndex
  
  
  def findStopCodon(dna, startIndex,stopCodon):
        """
        dna: a string of ATGC characters representing the nucleotides of a DNA molecule
        startIndex: index where the start codon is found in the DNA string. 
        stopCodon: a string of three characters, either "TAA", "TGA", or "TAG" , which are the stop codons in mammals
        stopIndex: output of function. Also the index where the stop codon is found. If no stop codon is found, the stopIndex is given the value None
        """
    dna = dna.upper() # ensuring that all letters of the dna string are uppercase.
    dna_length = len(dna)
    stopIndex = None
    
    for i in range(startIndex + 3,3,dna_length-3):  #  slicing through the dna string to see if any substring matches with the stop codon, starting from the startIndex
        if dna[i:i+3] == stopCodon:
            stopIndex = i
            break
                
    return stopIndex
  
    
 def find_Stop_Index(dna, startIndex):
    """
    This function is modified to find the best stop codon. Since there is more than one type of stop codon, we are interested in getting the index of the stop codon that occurs first.
    
    dna:  a string of ATGC characters representing the nucleotides of a DNA molecule
    startIndex: index where the start codon is found in the DNA string
    FinalStopIndex: output of function. Also the index where the first stop codon is found. If no stop codon is found, the stopIndex is given the value None
    """
    stopCodons = ["TAA", "TAG", "TGA"]
    stopIndices = []
    
    for stopCodon in stopCodons:
        stopIndex = findStopCodon(dna, startIndex, stopCodon) # Using stop codon function  to find each stop index        
        if stopIndex != None:
            stopIndices.append(stopIndex)   #Appends any found stop index for each of the three stop codons
    
    FinalStopIndex = None
    
    if stopIndices != []: # checks if any stop index was appended to take the minimum position
        FinalStopIndex = min(stopIndices)        
    return FinalStopIndex
  
    
  def findGene(dna):
    """
    dna: a string of ATGC characters representing the nucleotides of a DNA molecule
    gene: a string of ATGC characters representing the nucleotides of a gene molecule found in the given dna molecule
    """
    startIndex = findStartCodon(dna,0) # finds the start codon in the dna and returns its index
  
    if startIndex == None:
        return "No gene"   # If no start index is found then there is no gene
        
    stopIndex = find_Stop_Index(dna,startIndex)   # finds the stop codon in the dna and returns its index
    if stopIndex == None:
        return "No gene"   # If no stop codon is found, then there is no gene.
    else:
        gene = dna[startIndex : stopIndex+3]  # If both start and stop codons were found, then the gene is obtained by slicing the dna molecule from the start index to the stop index
   
    return gene
  
    
  def findGene_v2(dna, startIndex):
    """
    findGene_v2 is is used to find genes from any position along the DNA string by specifying the startIndex as a parameter
    dna: a string of ATGC characters representing the nucleotides of a DNA molecule
    startIndex: index where the gene should be searched from
    gene: a string of ATGC characters representing the nucleotides of a gene molecule found in the given dna molecule
    """
    startIndex = findStartCodon(dna,startIndex) # finds the start codon in the dna and returns its index
  
    if startIndex == None:
        return "No gene"   # If no start index is found then there is no gene
        
    stopIndex = find_Stop_Index(dna,startIndex)   # finds the stop codon in the dna and returns its index
    if stopIndex == None:
        return "No gene"   # If no stop codon is found, then there is no gene.
    else:
        gene = dna[startIndex : stopIndex+3]  # If both start and stop codons were found, then the gene is obtained by slicing the dna molecule from the start index to the stop index
   
    return gene

  
  def findAllGenes(dna):
    """
    To find all genes in the dna molecule
    """
    
    StartIndex = 0 # set start index
    genes = [] # initialize list where gene molecules will be appended
    gene_locations = [] # initialize list where gene indices will be appended
    
    while StartIndex != None: # looping over the dna molecule to find genes
        
        current_gene = findGene_v2(dna, StartIndex) # finding a gene fron start Index
        if current_gene == "No gene": # if no gene is found, the loop breaks and only already found genes are considered as existent genes
            break
            
        genes.append(current_gene) # append any gene found from startIndex position
        gene_locations.append(dna.find(current_gene)) # append any gene index found from startIndex position 
        
        
        start_here = dna.find(current_gene) + len(current_gene)
        StartIndex = find_Stop_Index(dna, start_here) # set the new start index , if no more start index is found, the while loop breaks
            
    results = (genes, gene_locations) # genes ans gene_locations are both of equal length. If no gene is found, both are an empty list
    return results
  
    
## Testing the code
# DNA = readfile (or dna string)
# Allgenes , gene_locations = findAllGenes(DNA)

#for gene in Allgenes:
 #   print(gene,"\n")
