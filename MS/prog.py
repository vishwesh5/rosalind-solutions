A = sorted(map(int, "".join(map(lambda x: x.rstrip(), list(open("dat"))[1:])).split()))
for n in A:
    print n,
