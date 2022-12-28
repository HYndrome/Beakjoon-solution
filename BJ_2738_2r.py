n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i, j in zip(a, b):
    print(*list(x + y for x, y in zip(i, j)))