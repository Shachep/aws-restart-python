# Store the human preproinsulin sequence in a variable
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements
lsInsulin = preproInsulin[0:24]
bInsulin = preproInsulin[24:54]
cInsulin = preproInsulin[54:89]
aInsulin = preproInsulin[89:110]

insulin = bInsulin + aInsulin

# Printing preproinsulin to console using sequence formatting
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to console using concatenated string
print("The sequence of human insulin, chain a: " + aInsulin)
# Calculating the molecular weight of insulin
# Creating a list of the amino acid weights
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Count the number of each amino acids
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}

# Multiply the count by the weight
molecularWeightInsulin = sum({x: aaCountInsulin[x] * aaWeights[x] for x in
aaCountInsulin}.values())

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# Actual molecular weight calculation with error percentage
molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))