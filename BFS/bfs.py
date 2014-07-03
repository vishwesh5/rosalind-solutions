from collections import deque

lines = map(lambda x: x.rstrip(), list(open("inp.dat")))
get_nums = lambda x: map(int, x.split())
n, m = get_nums(lines[0])

G = []
for i in range(n+1):
    row = [0] * (n+1)
    G.append(row)

for i in range(m):
    [u, v] = get_nums(lines[1+i])
    G[u][v] = 1

# Now that we have our adjacency matrix G, we can perform a BFS on it in order
# to count the number of edges

distances = [float('inf')] * (n+1)
distances[1] = 0
queue = deque()

# We need to make sure that each vertex is visited once to avoid endless looping
# in the case of a cycle in the graph.
has_checked_edge_dict = {}

queue.appendleft((1, G[1]))
while len(queue) > 0:
    idx, u = queue.pop()
    for i in range(1, n+1):
        if u[i] == 1:
            if not (idx, i) in has_checked_edge_dict:
                has_checked_edge_dict[(idx, i)] = True
                if distances[idx] + 1 < distances[i]:
                    distances[i] = distances[idx] + 1
                queue.appendleft((i, G[i]))

for i in range(1, n+1):
    elem = distances[i]
    if elem == float('inf'):
        print -1,
    else:
        print elem,
