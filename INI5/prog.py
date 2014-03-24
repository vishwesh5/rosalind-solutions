lines = list(open("file.txt"))

for i in range(1, len(lines), 2):
    print lines[i],
