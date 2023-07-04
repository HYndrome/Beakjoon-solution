# bfs 최단거리
import sys
from collections import deque
# 가로, 세로 입력 받기
i_n, i_m = map(int, sys.stdin.readline().split())
# 목표지점(bfs 상 시작점) (x, y) 형태
target = (0, 0)
# 입력 받은 그래프를 저장할 빈 리스트
graph = []
# 방문 처리 및 출력 리스트 (초기값 -1, 도달할 수 없는 위치 처리 쉽게하기 위함)
visited = [[-1] * i_m for _ in range(i_n)]
# graph 입력 받기
for y in range(i_n):
    ls_x = list(map(int, sys.stdin.readline().split()))
    for x in range(i_m):
        # 입력 받은 값이 2이면 target값 지정 및 visited 0 처리
        if ls_x[x] == 2:
            target = (x, y)
            visited[y][x] = 0
        # 입력 받은 값이 0이면 visited 0 처리
        if ls_x[x] == 0:
            visited[y][x] = 0
    graph.append(ls_x)
# 가로 세로 움직이는 값
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# bfs
que = deque([target])
while que:
    x, y = que.popleft()
    for d in delta:
        nx = x + d[0]
        ny = y + d[1]
        if (0 <= nx < i_m) and (0 <= ny < i_n):
            if graph[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                que.append((nx, ny))
# 값 출력
for y in range(i_n):
    print(*visited[y])