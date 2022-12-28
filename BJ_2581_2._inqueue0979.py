import sys

min = int(sys.stdin.readline().rstrip())
max = int(sys.stdin.readline().rstrip())

nums = [i for i in range(0, max + 1)]
primes = []
nums[1] = 0
sum = 0

for i in range(0, max + 1):
    if nums[i] == 0: continue
    
    for j in range(i * 2, max + 1, i):
        nums[j] = 0

for i in range(min, max + 1):
    if nums[i] != 0: 
        primes.append(i)
        sum = sum + i

if sum != 0:
    print(sum)
    print(primes[0])
else:
    print(-1)
