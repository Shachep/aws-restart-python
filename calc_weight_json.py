import jsonFileHandler

data = jsonFileHandler.readJsonFile('insulin.json')

if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    
    # Define amino acid weights dictionary directly
    aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
                'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 
                'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 
                'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19}
    
    # Count amino acids in insulin
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A', 'C',
    'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
    'V', 'W', 'Y']}
    
    # Calculate molecular weight
    molecularWeightInsulin = sum({x: aaCountInsulin[x] * aaWeights[x] for x in aaCountInsulin}.values())
    
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print("Error percentage: " + str(((molecularWeightInsulin - 5807.63) / 5807.63) * 100))
else:
    print("Error reading JSON file.")