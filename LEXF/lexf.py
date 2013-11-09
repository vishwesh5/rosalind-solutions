from itertools import combinations_with_replacement, permutations

ordering = "J W X M N I F C G".split(" ")
print ordering
indices = {}

for i in range(0, len(ordering)):
    indices[ordering[i]] = i

possibles = []
for coms in combinations_with_replacement("".join(ordering), 3):
    for perms in permutations("".join(coms)):
        potential = "".join(perms)
        if not (potential in possibles):
            possibles.append(potential)

def lte(s, t):
    if s == t:
        return True
    idx = 0
    while s[idx] == t[idx]:
        idx += 1
    return indices[s[idx]] < indices[t[idx]]

""" Do a comparison sort, and since 10! is our worst case, even selection sort's
    O(n^2) running time will do"""
for i in range(0, len(possibles)-1):
    for j in range(i+1, len(possibles)):
        if lte(possibles[i], possibles[j]):
            possibles[i], possibles[j] = possibles[j], possibles[i]

for p in reversed(possibles):
    print p
