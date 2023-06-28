# BFS로 최단 시간 찾기
import sys
from collections import deque

i_m, i_n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(i_n)]
# 시작점 찾기
ls_init = []
for y in range(i_n):
    for x in range(i_m):
        if graph[y][x] == 1:
            ls_init.append((x, y))
# bfs
delta = [(0, 1), (0, -1), (1, 0), (-1,0)]
que = deque(ls_init)
while que:
    start = que.popleft()
    for i in range(4):
        nx = start[0] + delta[i][0]
        ny = start[1] + delta[i][1]
        if 0 <= nx < i_m and 0 <= ny < i_n:
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[start[1]][start[0]] + 1
                que.append((nx, ny))
# 결과 확인 및 출력
max_date = 0
tomato_all = True
for y in range(i_n):
    if tomato_all == False:
        break
    for x in range(i_m):
        if graph[y][x] == 0:
            tomato_all = False
            break
        if graph[y][x] > max_date:
            max_date = graph[y][x]
if tomato_all == False:
    print(-1)
else:
    print(max_date - 1)