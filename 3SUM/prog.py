def get_indices(A):
    Nums = {}
    n = len(A)
    for i in range(0, n):
        Nums[A[i]] = i
    for i in range(0, n):
        for j in range(0, n):
            rhs = -(A[i] + A[j])
            if rhs in Nums:
                k = Nums[rhs]
                indices = [i, j, k]
                indices.sort()
                [p, q, r] = indices
                if p < q < r:
                    return (1+p, 1+q, 1+r)
    return -1

lines = map(lambda x: x.rstrip(), list(open("inp.dat")))

[k, n] = map(int, lines[0].split())

for i in range(0, k):
    A = map(int, lines[1+i].split())
    idx = get_indices(A)
    if idx == -1:
        print idx
    else:
        p, q, r = idx
        print p,q,r
