N = set(range(1, 10001))
n = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    n.add(i)
self_n = sorted(N - n)
for i in self_n:
    print(i)