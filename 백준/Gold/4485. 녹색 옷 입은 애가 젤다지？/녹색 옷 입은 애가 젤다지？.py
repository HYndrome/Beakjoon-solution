import sys
import heapq

INF = int(1e9)
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
i_test = 0
while True:
    i_t = int(sys.stdin.readline())
    i_test += 1
    if i_t == 0:
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(i_t)]
    distance = [[INF] * i_t for _ in range(i_t)]

    def dijkstra(start):
        que = []
        heapq.heappush(que, (graph[0][0], start))
        distance[start[1]][start[0]] = graph[0][0]
        while que:
            dist, now = heapq.heappop(que)
            if distance[now[1]][now[0]] < dist:
                continue
            for dx, dy in move:
                nx = now[0] + dx
                ny = now[1] + dy
                if (0 <= nx < i_t) and (0 <= ny < i_t):
                    cost = dist + graph[ny][nx]
                    if cost < distance[ny][nx]:
                        distance[ny][nx] = cost
                        heapq.heappush(que, (cost, (nx, ny)))

    dijkstra((0, 0))

    print(f'Problem {i_test}: {distance[i_t - 1][i_t - 1]}')