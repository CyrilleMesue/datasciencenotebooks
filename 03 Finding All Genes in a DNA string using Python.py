def findStartCodon(dna, start_location):
    dna = dna.upper()
    startCodon = "ATG"
    dna_length = len(dna)
    startIndex = None
    for i in range(start_location,dna_length-3):
        if dna[i:i+3] == startCodon:
            startIndex = i
            break
    return startIndex
  
  
  def findStopCodon(dna, startIndex,stopCodon):
    dna = dna.upper()
    dna_length = len(dna)
    stopIndex = None
    
    for i in range(startIndex + 3,dna_length-3):
        if dna[i:i+3] == stopCodon:
            stopIndex = i
            break
                
    return stopIndex

  def findStopCodon(dna, startIndex,stopCodon):
    dna = dna.upper()
    dna_length = len(dna)
    stopIndex = None
    
    for i in range(startIndex + 3,dna_length-3):
        if dna[i:i+3] == stopCodon:
            if (i - startIndex) % 3 == 0:
                stopIndex = i
                break
                
    return stopIndex
  
  def find_Stop_Index_v1(DNA, startIndex):
    stopCodons = ["TAA", "TAG", "TGA"]
    stopIndices = []
    
    for stopCodon in stopCodons:
        stopIndex = findStopCodon(DNA, startIndex, stopCodon)
        stopIndices.append(stopIndex)
    
    return stopIndices
  
 def find_Stop_Index_v2(DNA, startIndex):
    stopCodons = ["TAA", "TAG", "TGA"]
    stopIndices = []
    
    for stopCodon in stopCodons:
        stopIndex = findStopCodon(DNA, startIndex, stopCodon)
        if stopIndex != None:
            stopIndices.append(stopIndex)
    
    FinalStopIndex = None
    
    if stopIndices != []:
        FinalStopIndex = min(stopIndices)
        
    return FinalStopIndex
  
  def findGene(dna):
    dna.upper()
    startIndex = findStartCodon(dna,0)
  
    if startIndex == None:
        return "No gene"
        
    stopIndex = find_Stop_Index_v2(dna,startIndex)    
    if stopIndex == None:
        return "No gene"
    else:
        gene = dna[startIndex : stopIndex+3]
   
    return gene
  
  def findGene_v2(dna, startIndex):
    dna.upper()
  
    if startIndex == None:
        return "No gene"
        
    stopIndex = find_Stop_Index_v2(dna,startIndex)    
    if stopIndex == None:
        return "No gene"
    else:
        gene = dna[startIndex : stopIndex+3]
   
    return gene
  
  def findAllGenes(dna):
    
    genes = []
    gene_locations = []
    
    ii = 0
    while ii < len(dna) -3:
        
        StartIndex = findStartCodon(dna, ii)
        current_gene = findGene_v2(dna, StartIndex)
        if current_gene == "No gene":
            break
            
        genes.append(current_gene)
        gene_locations.append(dna.find(current_gene))
        
        
        start_here = dna.find(current_gene) + len(current_gene)
        ii = start_here
        
            
    results = (genes, gene_locations)
    return results
  
  def findAllGenes(dna):
    StartIndex = findStartCodon(dna,0)
    genes = []
    gene_locations = []
    
    for ii in range(len(dna)-5):
        
        current_gene = findGene_v2(dna, StartIndex)
        if current_gene == "No gene":
            break
            
        genes.append(current_gene)
        gene_locations.append(dna.find(current_gene))
        
        
        start_here = dna.find(current_gene) + len(current_gene)
        StartIndex = findStartCodon(dna, start_here)
            
    results = (genes, gene_locations)
    return results
  
  
Allgenes , gene_locations = findAllGenes(DNA)

for gene in Allgenes:
    print(gene,"\n")
