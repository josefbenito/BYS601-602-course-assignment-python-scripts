#parsing information from GenBank

InFile = file("mitogenome.gb","r") 
OutFile = file("mitogenome_results.txt","w")

a = InFile.readlines() #gives out a list

z = len(a)

for j in range(z):
    spl = a[j].split()
    print spl
    y = len(spl)
    for i in range(y):
        if (spl[i] == "DEFINITION"):
            b = 0
            c = 0
            d = 0
            e = 0
            output = a[j].split()
            rec = ""
            rec += " ".join(output[1: ])
            print '\033[4m' + "Definition:" + '\033[0m', rec
            OutFile.write("Definition: ")
            OutFile.write(rec)
            OutFile.write("\n")
       
        if (spl[i] == "AUTHORS" and b == 0):
            output = a[j].split()
            b = 1
            rec = ""
            rec += " ".join(output[1: ])
            for k in range(1,z):
                rec2 = a[j+k].split() 
                if (rec2[0] == "TITLE"):
                    break
                else:
                    rec += " ".join(rec2[0: ])
            print '\033[4m' + "Authors:" + '\033[0m', rec
            OutFile.write("Authors: ")
            OutFile.write(rec)
            OutFile.write("\n")
    
        if (spl[i] == "TITLE" and c == 0 ):
            output = a[j].split()
            c = 1
            rec = ""
            rec += " ".join(output[1: ])
            for k in range(1,z):
                rec2 = a[j+k].split() 
                if (rec2[0] == "JOURNAL"):
                    break
                else:
                    rec += " ".join(rec2[0: ])
            print '\033[4m' + "Title:" + '\033[0m', rec
            OutFile.write("Title: ")
            OutFile.write(rec)
            OutFile.write("\n")
            
        if (spl[i] == "ACCESSION"):
            output = a[j].split()
            rec = ""
            rec += " ".join(output[1: ])
            print '\033[4m' + "Accession:" + '\033[0m', rec
            OutFile.write("Accession: ")
            OutFile.write(rec)
            OutFile.write("\n")
            
        if (spl[i] == "gene" and d == 0):
            d = 1
            output = a[j].split()
            rec = ""
            rec += " ".join(output[1: ])
            rec2 = rec.split("..")
            print '\033[4m' + "Gene start and stop locations:" + '\033[0m', rec2[0], "to", rec2[1]
            OutFile.write("Gene start and stop locations: ")
            OutFile.write(rec2[0])
            OutFile.write(" to ")
            OutFile.write(rec2[1])
            OutFile.write("\n")
            
        if (spl[i] == "CDS" and e == 0):
            e = 1
            output = a[j].split()
            rec = ""
            rec += " ".join(output[1: ])
            rec2 = rec.split("..")
            print '\033[4m' + "CDS start and stop locations:" + '\033[0m', rec2[0], "to", rec2[1], "\n"
            OutFile.write("CDS start and stop locations: ")
            OutFile.write(rec2[0])
            OutFile.write(" to ")
            OutFile.write(rec2[1])
            OutFile.write("\n")
            OutFile.write("\n")
            
InFile.close()
OutFile.close()