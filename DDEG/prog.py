lines = list(open("inp.dat"))
lines = map(lambda x: x.rstrip(), lines)

def get_tuple(line):
    a, b = line.split()
    return [int(a), int(b)]

def num_nonzero_entries(u):
    nonzeros = 0
    for elem in u:
        if elem != 0:
            nonzeros += 1
    return nonzeros

n, m = get_tuple(lines[0])

G = []
for _ in range(n):
    zeros = map(lambda x: 0, range(n))
    G.append(zeros)

for i in range(1, len(lines)):
    u, v = get_tuple(lines[i])
    G[u-1][v-1] = 1
    G[v-1][u-1] = 1

deg = []

for vert in G:
    deg.append(num_nonzero_entries(vert))

for i in range(n):
    degree = 0
    for j in range(n):
        if G[i][j] != 0:
            degree += deg[j]
    print degree,
