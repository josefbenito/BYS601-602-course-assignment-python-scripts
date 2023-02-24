#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import numpy as np
with open('JN_blosom50.txt') as f:
    content = [line.split() for line in f]
x = np.array(content)
matrix = x.astype(float)
print matrix
#print content
print "This program will align two sequencses with the Blosum50 matrix"

seq1 = 'IQIFSFIFRQEWNDA'
seq2 = 'QIFFFFRMSVEWND'
abet = 'ARNDCQEGHILKMFPSTWYV'


def ScoringMatrix(matrix,abet,seq1,seq2, gp= -16):
	L1,L2 = len(seq1), len(seq2)
	scoremat = zeros( (L1+1, L2+1), int) #this forms a 16X15 matrix of zeros
	arrow = zeros( (L1+1, L2+1), int) #this forms a 16X15 matrix of zeros
	#create first row and first column
	scoremat[0] = arange(L2 + 1)* gp  #replaces first row with gap penalty (in increments of -2)
	scoremat[:,0] = arange(L1 + 1) * gp  #replaces first column with gap penalty row (in increments of -2)
	arrow[0]= ones(L2 + 1) #replaces first row with all 1's
	
	
	
	for i in range(1, L1+1):
		for j in range(1, L2+1):
			f = zeros(3)  #makes an array all 3 zeros. Note they are floats unless you say otherwise
			f[0] = scoremat[i - 1,j] + gp 
			f[1] = scoremat[i,j-1] + gp
			if seq1[i-1] == seq2[j-1]:
			   f[2] = scoremat[i-1,j-1] + 5
			else:
			   f[2] = scoremat[i-1,j-1] - 1
                
			scoremat[i,j] = f.max() 
			arrow[i,j] = f.argmax() 
	return scoremat, arrow 
							
def Backtrace(arrow, seq1, seq2 ):
	st1, st2 = "",""  
	v,h = arrow.shape  
	ok = 1  
	v-=1   
	h-=1  
	while ok:   # When ok = 1, as long as this is a true value and it will procede with what follows
		if arrow[v,h] == 0: 
			st1 += seq1[v-1] # This is the same as st1 = st1 + seq1[v-1]
			st2 += '-' # This is the same as st2 = st2 + "-"
			v -= 1 #same as v = v - 1
		elif arrow[v,h] == 1:
			st1 = '-'
			st2 = seq2[h-1]
			h -= 1 # Same as h = h - 1
		elif arrow[v,h] == 2:
			st1 += seq1[v-1] #This is the same as st1 = st1 + seq1[v-1]
			st2 += seq2[h-1] ##This is the same as st2 = st2 + seq1[h-1]
			v -= 1
			h -= 1
		if v == 0 and h ==0: #this is a new if line
			ok = 0  # This could also be written as ok = False
	# reverse the stsrings
	st1 = st1[::-1] #reads all the string but backwards one at a time
	
	st2 = st2[::-1] # Same as above
	return st1, st2  

#Now you can use the functions and print the output

scoremat, arrow = ScoringMatrix(matrix,abet,seq1,seq2, gp=-2)
print scoremat, "\n\n", arrow

align1 , align2 = Backtrace( arrow, seq1, seq2 )
print align1,"\n", align2
