# Python Software to Process Human Insulin Sequence

# Importing the file contents
with open('preproinsulin-seq-clean.txt') as f:
    preproinsulin = f.read().strip()

# Printing out the preproinsulin sequence length and content
print("Preproinsulin length:", len(preproinsulin))
print("Preproinsulin sequence:", preproinsulin)

# Loading the individual insulin sections
with open('lsinsulin-seq-clean.txt') as f:
    lsinsulin = f.read().strip()

with open('binsulin-seq-clean.txt') as f:
    binsulin = f.read().strip()

with open('cinsulin-seq-clean.txt') as f:
    cinsulin = f.read().strip()

with open('ainsulin-seq-clean.txt') as f:
    ainsulin = f.read().strip()

# Verifying the lengths of each segment
print("\nSegment Lengths Verification:")
print("lsinsulin length:", len(lsinsulin))
print("binsulin length:", len(binsulin))
print("cinsulin length:", len(cinsulin))
print("ainsulin length:", len(ainsulin))