N = 28
k = 5

rabbits = [1, 1]

for i in range(3, N+1):
    num_rabbits = rabbits[i-2] + k*rabbits[i-3]
    rabbits.append(num_rabbits)

print rabbits[-1]
