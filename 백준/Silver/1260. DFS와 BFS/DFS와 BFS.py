import sys
from collections import deque

# 입력 받기
i_n, i_m, i_v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(i_n + 1)]
for edge in range(i_m):
    node1 , node2  = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
# 리스트 정렬
for node in range(i_n + 1):
   graph[node].sort()
# DFS (재귀)
visited = [False] * (i_n + 1)
ls_print = []
def dfs(current_node):
    visited[current_node] = True
    ls_print.append(current_node)
    for node in graph[current_node]:
        if visited[node] == False:
         dfs(node)
dfs(i_v)
print(*ls_print)

# BFS
visited = [False] * (i_n + 1)
ls_print = []
visited[i_v] = True
ls_print.append(i_v)
que = deque([i_v])
while que:
   current_node = que.popleft()
   for node in graph[current_node]:
      if visited[node] == False:
         visited[node] = True
         ls_print.append(node)
         que.append(node)
print(*ls_print)