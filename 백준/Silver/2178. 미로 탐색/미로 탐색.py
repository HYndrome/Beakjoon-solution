# bfs 최단거리
import sys
from collections import deque

# 입력
i_n, i_m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(i_n)]
# bfs delta 탐색
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = (0, 0)
que = deque()
que.append(start)
while que:
    x, y = que.popleft()
    if x == i_m - 1 and y == i_n - 1:
        break
    for d in range(4):
        nx = x + delta[d][0]
        ny = y + delta[d][1]
        if 0 <= nx < i_m and 0 <= ny < i_n:
            # 방문 확인
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                que.append((nx, ny))
print(graph[i_n - 1][i_m -1])