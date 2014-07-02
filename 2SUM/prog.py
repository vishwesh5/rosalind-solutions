"""
1) Create an (10^5)x2 matrix M, where every entry is zero
2) For each a in A at index i, let n = abs(a)
    2.1) Set M[n][0] = i if n != a
         if M[n][1] != 0
            output p, q
    2.2) Set M[n][1] = i if n == a
         if M[n][0] != 0
            output p, q
"""

def get_indices(A):
    M = []
    for k in range(0, 10**5):
        M.append([-1, -1])
    for i in range(0, len(A)):
        a = A[i]
        n = abs(a)
        if a == n:
            M[n][1] = i
            if M[n][0] != -1 and (M[n][1] != M[n][0]):
                return (1+min(M[n]), 1+max(M[n]))
        if a == -n:
            M[n][0] = i
            if M[n][1] != -1 and (M[n][1] != M[n][0]):
                return (1+min(M[n]), 1+max(M[n]))
    return -1

lines = map(lambda x: x.rstrip(), list(open("inp.dat")))
_1, _2 = lines[0].split()
k = int(_1)
n = int(_2)

for i in range(k):
    A = map(lambda x: int(x), lines[1+i].split())
    i = get_indices(A)
    if i == -1:
        print -1
    else:
        a, b = i
        print a, b
