import sys, heapq


INF = int(1e9)
i_n, i_m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(i_n + 1)]
distance = [INF] * (i_n + 1)
for i in range(i_m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append((end, 1))
    graph[end].append((start, 1))

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
i_bacon = INF
i_index = 0
for i in range(1, i_n + 1):
    dijkstra(i)
    i_sum = sum(distance[1:])
    if i_sum < i_bacon:
        i_bacon = i_sum
        i_index = i
    distance = [INF] * (i_n + 1)
print(i_index)