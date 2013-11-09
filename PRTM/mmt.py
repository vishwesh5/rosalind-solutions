data = {}
data['A'] = 71.03711
data['C'] = 103.00919
data['D'] = 115.02694
data['E'] = 129.04259
data['F'] = 147.06841
data['G'] = 57.02146
data['H'] = 137.05891
data['I'] = 113.08406
data['K'] = 128.09496
data['L'] = 113.08406
data['M'] = 131.04049
data['N'] = 114.04293
data['P'] = 97.05276
data['Q'] = 128.05858
data['R'] = 156.10111
data['S'] = 87.03203
data['T'] = 101.04768
data['V'] = 99.06841
data['W'] = 186.07931
data['Y'] = 163.06333 

def weighted_sum(protein_string):
    total = 0
    for ch in protein_string:
        total += data[ch]
    print round(total, 3)
