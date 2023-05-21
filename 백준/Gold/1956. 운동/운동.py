import sys


i_v, i_e = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (i_v + 1) for _ in range(i_v + 1)]
for i in range(i_e):
    start, end, distance = map(int, sys.stdin.readline().split())
    graph[start][end] = distance

for k in range(1, i_v + 1):
    for y in range(1, i_v + 1):
        for x in range(1, i_v + 1):
            graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

cycle_min = INF
for i in range(1, i_v):
    cycle_v = graph[i][i]
    if cycle_v < cycle_min:
        cycle_min = cycle_v

if cycle_min == INF:
    print(-1)
else:
    print(cycle_min)