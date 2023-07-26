# 다익스트라 최단거리
import sys, heapq

# N, M, X 입력
i_n, i_m, i_x = map(int, sys.stdin.readline().split())
# 그래프 입력 [(도착노드, 거리)] 형태로 입력
graph = [[] for _ in range(i_n + 1)]
for road in range(i_m):
    start, end, distance = map(int, sys.stdin.readline().split())
    graph[start].append((end, distance))
# 다익스트라
# 시작점을 입력 받아 다른 노드까지의 최단거리 테이블을 return
INF = int(1e9)
def dijkstra(start):
    distance_table = [INF] * (i_n + 1)
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
    return distance_table

# 전체 노드에 대하여 다익스트라를 적용하여 n부터 x, x부터 n까지의 거리 계산
distance_n_to_x = [0] * (i_n + 1)
distance_x_to_n = [0] * (i_n + 1)
for student in range(1, i_n + 1):
    if student == i_x:
        distance_x_to_n = dijkstra(student)
    else:
        distance_n_to_x[student] = dijkstra(student)[i_x]
distance_n_to_x_to_n = [0] * (i_n + 1)
for student in range(1, i_n + 1):
    distance_n_to_x_to_n[student] = distance_n_to_x[student] + distance_x_to_n[student]
# 최댓값 출력
max_distance = max(distance_n_to_x_to_n[1:])
print(max_distance)