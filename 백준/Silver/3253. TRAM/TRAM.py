import sys
import heapq

i_n, i_a, i_b = map(int, sys.stdin.readline().split())

INF = int(1e9)
graph = [[] for _ in range(i_n + 1)]
distance = [INF] * (i_n + 1)

for i in range(i_n):
    ls_input = list(map(int, sys.stdin.readline().split()))
    if ls_input[0] == 0:
        pass
    else:
        graph[i+1].append((ls_input[1], 0))
        if ls_input[0] >= 2:
            for path in ls_input[2:]:
                graph[i+1].append((path, 1))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for path in graph[now]:
            cost = dist + path[1]
            if cost < distance[path[0]]:
                distance[path[0]] = cost
                heapq.heappush(que, (cost, path[0]))

dijkstra(i_a)

if distance[i_b] == INF:
    print(-1)
else:
    print(distance[i_b])