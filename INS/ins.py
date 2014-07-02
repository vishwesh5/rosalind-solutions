n = int(raw_input())

nums = map(lambda x: int(x), raw_input().split())
swaps = 0

for i in range(1, n):
    k = i
    while k > 0 and nums[k] < nums[k-1]:
        tmp = nums[k]
        nums[k] = nums[k-1]
        nums[k-1] = tmp
        k -= 1
        swaps += 1

print swaps
