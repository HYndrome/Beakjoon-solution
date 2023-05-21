import sys


i_n, i_m, i_r = map(int, sys.stdin.readline().split())
ls_items = [0] + list(map(int, sys.stdin.readline().split()))
INF = int(1e9)
graph = [[INF] * (i_n + 1) for _ in range(i_n + 1)]
for i in range(i_r):
    start, end, distance = map(int, sys.stdin.readline().split())
    graph[start][end] = distance
    graph[end][start] = distance
for y in range(1, i_n + 1):
    for x in range(1, i_n + 1):
        if x == y:
            graph[y][x] = 0

for k in range(1, i_n + 1):
    for y in range(1, i_n + 1):
        for x in range(1, i_n + 1):
            graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

items_max = 0
for y in range(1, i_n + 1):
    items_y = 0
    for x in range(1, i_n + 1):
        if graph[y][x] <= i_m:
            items_y += ls_items[x]
    if items_y > items_max:
        items_max = items_y

print(items_max)