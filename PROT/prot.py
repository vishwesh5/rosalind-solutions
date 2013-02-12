codon_table = list(open("codon_table.dat"))
codons = {}
for e in codon_table:
    tokens = e.split(" ")
    codons[tokens[0]] = tokens[1].rstrip()

protein_string = list(open("data.txt"))[0][:-1] # strip off that newline
result = ""
for i in range(0, len(protein_string)-3, 3):
    seg = protein_string[i:i+3]
    val = codons[seg]
    if val != "Stop":
        result += codons[seg]
    else:
        break

print result
