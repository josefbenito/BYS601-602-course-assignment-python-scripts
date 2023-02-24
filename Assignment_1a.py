#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Script #1a: SwissVar Domain associated with pathogenic diseases
#Source: homo_sapiens_variation.txt, 9606_v31.tsv
#Input: No command line input. 
#Output: List of protein domains with observed variations (stop gain/loss or missense) and associated with pathogenic diseases

outFile = file("Pathogenic_domains.tsv","w")
pfam = file("9606_v31.tsv")
swissvar = file("homo_sapiens_variation.txt")
	
domainData = [] 

for line in pfam:
	if line.startswith("#"):
		continue
	else:
		b = line.strip().split("\t")
		domainData.append(b[0:7]) 
        
pfam.close()

runFlag = False
swissData = []

for line in swissvar:
	if runFlag == True:
         a = line.strip().split()
         try:
             if (a[6] == "pathogenic" and len(a[2]) <= 11 and a[7] != "-"):
                 swissData.append(a[0:8])                         
         except IndexError:
             continue
        
	elif line.startswith("_"):
		runFlag = True
	if runFlag == True and line.startswith("-"): 
		break

uniqueData = []

for i in swissData:
    if i not in uniqueData:
        uniqueData.append(i)
        
print swissData
            
swissvar.close()

#print "hmm acc\thmm name\tGene Name\tAC\tVariant AA Change\tConsequence Type\tClinical Significance\tPhenotype/Disease"
outFile.write("hmm acc\thmm name\tGene Name\tAC\tVariant AA Change\tConsequence Type\tClinical Significance\tPhenotype/Disease\n")

for element in domainData: 
    for entry in uniqueData:
        if int(entry[2][5:-3]) >= int(element[3]) and int(entry[2][5:-3]) <= int(element[4]):
            variant = " ".join(entry[4:6])
            #print element[5], element[6], entry[0], entry[1], entry[2], variant, entry[6], entry[7]
            outFile.write(element[5]+"\t"+element[6]+"\t"+entry[0]+"\t"+entry[1]+"\t"+entry[2]+"\t"+variant+"\t"+entry[6]+"\t"+entry[7]+"\n")
      
outFile.close()
            
    

