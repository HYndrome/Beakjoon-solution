# 다익스트라 최단거리
import sys, heapq

# 양방향 그래프 입력
i_n, i_e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(i_n + 1)]
for i in range(i_e):
    v_a, v_b, distance = map(int, sys.stdin.readline().split())
    graph[v_a].append((v_b, distance))
    graph[v_b].append((v_a, distance))
waypoint1, waypoint2 = map(int, sys.stdin.readline().split())

# 다익스트라
# 시작점과 끝점을 입력 받아 최단 거리를 return
INF = int(1e9)
def dijkstra(start, end):
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
    return distance_table[end]

# 두정점을 반드시 거치면서 최단거리
# 최단거리는 반드시 둘 중 하나
# 1. 시작점 정점1 정점2 끝점
# 2. 시작점 정점2 정점1 끝점 
d_start_waypoint1 = dijkstra(1, waypoint1)
d_waypoint1_waypoint_2 = dijkstra(waypoint1, waypoint2)
d_waypoint2_end = dijkstra(waypoint2, i_n)

d_start_waypoint2 = dijkstra(1, waypoint2)
d_waypoint1_end = dijkstra(waypoint1, i_n)

d_start_waypoint1_waypoint2_end = d_start_waypoint1 + d_waypoint1_waypoint_2 + d_waypoint2_end
d_start_waypoint2_waypoint1_end = d_start_waypoint2 + d_waypoint1_waypoint_2 + d_waypoint1_end

min_distance = min(d_start_waypoint1_waypoint2_end, d_start_waypoint2_waypoint1_end )

# 도달할 수 없는 경우 최단 경로는 INF+a이므로 해당 예외 처리 및 출력
if min_distance >= INF:
    print(-1)
else:
    print(min_distance)