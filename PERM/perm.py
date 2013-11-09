from itertools import permutations
n = 6
array = range(1, n+1)

def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print fact(n)
for p in permutations(array):
    for e in p:
        print e,
    print ""
