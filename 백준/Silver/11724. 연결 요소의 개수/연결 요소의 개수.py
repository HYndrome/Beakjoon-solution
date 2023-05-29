import sys
from collections import deque


i_n, i_m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(i_n + 1)]
for i in range(i_m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [False] * (i_n + 1)
cnt = 0
def bfs(v):
    if visited[v] == False:
        visited[v] = True
        global cnt
        cnt += 1
        que = deque()
        que.append(v)
        while que:
            v = que.popleft()
            for v_connected in graph[v]:
                if visited[v_connected] == False:
                    visited[v_connected] = True
                    que.append(v_connected)
for v in range(1, i_n + 1):
    bfs(v)
print(cnt)