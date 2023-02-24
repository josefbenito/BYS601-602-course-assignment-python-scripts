#This program calculates the components of a buffer

try:    
    comp_num = int(raw_input("\nHow many components in your buffer: "))
except ValueError:
    print "\nInvalid entry! Enter only numbers"
    comp_num = int(raw_input("\nHow many components in your buffer: "))

comp=[]
conc=[]
mw=[]

for i in range(1,comp_num+1):
    comp.append(str(raw_input("\nWhat is your %d component: " %(i))))
    try:
        conc.append(float(raw_input("\nWhat is the concentration of your %d component in M: " %(i))))
    except ValueError:
        print "\nInvalid entry! Enter either whole number or decimal"
        conc.append(float(raw_input("\nWhat is the concentration of your %d component in M: " %(i))))
    try:
        mw.append(float(raw_input("\nWhat is the molecular weight of your %d component in gm/mole: " %(i))))
    except ValueError:
        print "\nInvalid entry! Enter either whole number or decimal"
        mw.append(float(raw_input("\nWhat is the molecular weight of your %d component in gm/mole: " %(i))))
    
vol = float(raw_input("\nWhat is the final volume of your buffer in mL: "))

print "\nThe components you entered: ",comp
print "The concentrations you entered: ",conc
print "The molecular weights you entered: ",mw
print "The final volume you entered: ",vol

comp_calc=[]

for i in range(0,comp_num):
    comp_calc.append(float(conc[i] * mw[i] * vol/1000))
    
result=[]

for i in range(0,comp_num):
    result.append(round(comp_calc[i],2))
    print "\nThe amount of " + comp[i] + " to weigh in gm: ", result[i]