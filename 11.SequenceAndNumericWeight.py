# Store the human preproinsulin sequence in a variable called preproinsulin:
# Fungsi dari backslash adalah untuk menyesuaikan dengan PEP8 mengenai tata cara penulisan python code yang baik

prepoInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:

lsInsulin =  "malwmrllpllallalwgpdpaaa"
bInsulin = 'fvnqhlcgshlvealylvcgergffytpkt'
cInsulin = "giveqcctsicslyqlenycn"
aInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

IsInsulin1 = prepoInsulin[0:24]
bInsulin1 = prepoInsulin[24:54]
cInsulin1 = prepoInsulin[54:89]
aInsulin1 = prepoInsulin[89:110]

print(f'IsInsulin: {lsInsulin}, Panjang karakter: {len(lsInsulin)}')
print(f'bInsulin: {bInsulin}, Panjang karakter: {len(bInsulin)}')
print(f'aInsulin: {aInsulin}, Panjang karakter: {len(aInsulin)}')
print(f'cInsulin: {cInsulin}, Panjang karakter: {len(cInsulin)}')

print("=============================================================")

print(f'IsInsulin: {IsInsulin1}, Panjang karakter: {len(IsInsulin1)}')
print(f'bInsulin: {bInsulin1}, Panjang karakter: {len(bInsulin1)}')
print(f'aInsulin: {aInsulin1}, Panjang karakter: {len(aInsulin1)}')
print(f'cInsulin: {cInsulin1}, Panjang karakter: {len(cInsulin1)}')

print("===================        INSULIN      =====================")

insulin = aInsulin1 + bInsulin1
print(f'cInsulin: {insulin}, Panjang karakter: {len(insulin)}')


# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  


# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
print(aaCountInsulin)

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

# Rumus untuk menghitung error percentage
molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))