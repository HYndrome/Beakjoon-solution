# BFS가 최초로 도착한 지점이 최단거리라는 점을 이용
from collections import deque


i_x = int(input())

que = deque([i_x])
visited = [0] * (i_x + 1)
while que:
    current = que.popleft()
    if current == 1:
        break
    if current % 3 == 0 and visited[current // 3] == 0:
        que.append(current // 3)
        visited[current // 3] = visited[current] + 1
    if current % 2 == 0 and visited[current // 2] == 0:
        que.append(current // 2)
        visited[current // 2] = visited[current] + 1
    if visited[current - 1] == 0:
        que.append(current - 1)
        visited[current - 1] = visited[current] + 1
print(visited[1])
