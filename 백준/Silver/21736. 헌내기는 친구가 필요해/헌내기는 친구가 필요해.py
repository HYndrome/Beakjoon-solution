# bfs 완전탐색
import sys
from collections import deque

# 입력 및 시작지점 인덱스 구하기
i_n, i_m = map(int, sys.stdin.readline().split())
start = [0, 0]
graph = []
for y in range(i_n):
    graph_x = sys.stdin.readline().rstrip()
    graph.append(graph_x)
    if "I" in graph_x:
        start[0] = graph_x.index("I")
        start[1] = y
# bfs 델타 탐색
delta = ((1, 0), (0, -1), (-1, 0), (0, 1))
# 방문 처리 리스트
visited  = [[0] * i_m for y in range(i_n)]
# 만나는 사람 수 저장 변수
cnt_meet = 0
que = deque([start])
visited[start[1]][start[0]] = 1
while que:
    current = que.popleft()
    for i in range(4):
        nx = current[0] + delta[i][0]
        ny = current[1] + delta[i][1]
        if 0 <= nx < i_m and 0 <= ny < i_n:
            if graph[ny][nx] == "O" and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                que.append([nx, ny])
            if graph[ny][nx] == "P" and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                que.append([nx, ny])
                cnt_meet += 1
# 출력
if cnt_meet == 0:
    print("TT")
else:
    print(cnt_meet)