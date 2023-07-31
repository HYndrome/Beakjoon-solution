# 다익스트라 최단 경로
import sys, heapq

# 그래프 입력
i_V, i_E = map(int, sys.stdin.readline().split())
i_k = int(sys.stdin.readline())
graph = [[] for _ in range(i_V + 1)]
for e in range(i_E):
    i_u, i_v, i_w = map(int, sys.stdin.readline().split())
    graph[i_u].append((i_v, i_w))

# 다익스트라
INF = int(1e9)
distance_table = [INF] * (i_V + 1)
# 시작점을 입력 받아, distance_table에 최단 거리 update하는 함수
def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance_table[start] = 0
    while que:
        distance, current = heapq.heappop(que)
        if distance_table[current] < distance:
            continue
        for adjacent in graph[current]:
            cost = distance + adjacent[1]
            if cost < distance_table[adjacent[0]]:
                distance_table[adjacent[0]] = cost
                heapq.heappush(que, (cost, adjacent[0]))
    return
dijkstra(i_k)

# 출력
for vertex in range(1, i_V + 1):
    if distance_table[vertex] == INF:
        print("INF")
    else:
        print(distance_table[vertex])

