lines = map(lambda x: x.rstrip(), list(open("inp.dat")))

n = int(lines[0])
A = map(lambda x: int(x), lines[1].split())
m = int(lines[2])
B = map(lambda x: int(x), lines[3].split())

a = 0
b = 0

C = []

while a < n and b < m:
    if A[a] == min(A[a], B[b]):
        C.append(A[a])
        a += 1
    else:
        C.append(B[b])
        b += 1

if b == m:
    for i in range(a, n):
        C.append(A[i])
else:
    for i in range(b, n):
        C.append(B[i])

for c in C:
    print c,
