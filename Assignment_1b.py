#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Script #1b: Find Domain
#Source: Pathogenic_domains.tsv PFAM pathogenic data
#Input: Assignment_1b.py <source filename (str)> <domain hmm name (str)>
#Output: List of variations and associated diseases found in domain

import sys
filename = sys.argv[1]
hmm_acc = sys.argv[2]

inFile = file(filename)
outFile = file("Find_domain.tsv","w")

print "hmm acc\thmm name\tGene Name\tAC\tVariant AA Change\tConsequence Type\tClinical Significance\tPhenotype/Disease"
outFile.write("hmm acc\thmm name\tGene Name\tAC\tVariant AA Change\tConsequence Type\tClinical Significance\tPhenotype/Disease\n")
 
for line in inFile:
    if line.startswith("h"):
		continue
    else:
        data = line.strip().split("\t")
        
    if data[0] == hmm_acc:
            rec = "\t".join(data[0:8])
            print rec 
            outFile.write(rec + "\n")
    else:
		continue
            

