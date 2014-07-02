# Algorithm: Since our upper bound is 10^5, make an array of 10^5 elements
ints = [0] * (10**5)

lines = list(open("inp.dat"))
map(lambda x: x.rstrip(), lines)

_1, _2 = lines[0].split()
k = int(_1)
n = int(_2)

min_majority = 1 + (n / 2)

for i in range(1, k+1):
    str_array = lines[i].rstrip()
    elems = map(lambda x: int(x), str_array.split())
    found = False
    for e in elems:
        ints[e] += 1
        if ints[e] >= min_majority:
            found = True
            print e,
            break
    if not found:
        print -1,
    ints = [0] * (10**5)
