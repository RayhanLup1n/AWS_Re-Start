# Python3.6
# Coding: UTF-8


# Store the human preproinsulin sequence in a variable called preproinsulin:
# Fungsi dari backslash adalah untuk menyesuaikan dengan PEP8 mengenai tata cara penulisan python code yang baik

prepoInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:

IsInsulin = prepoInsulin[0:24]
bInsulin = prepoInsulin[24:54]
cInsulin = prepoInsulin[54:89]
aInsulin = prepoInsulin[89:110]
insulin = bInsulin + aInsulin

# Validate insulin variable
print(insulin)


pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)

seqCount_opt = ({x: float(insulin.count(x)) for x in pKR.keys()})
print(seqCount_opt)

pH = 0
while (pH <=14 ):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values()))) 
    
    print('{0:.2f}'.format(pH), netCharge)
    
    pH += 1