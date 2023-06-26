# BFS 최초 도착할 경우 최단거리
from collections import deque

i_n, i_k = map(int, input().split())
visited = [0] * 100001
que = deque([i_n])
while que:
    # 처음부터 같을 경우도 처리해줘야함
    if (visited[i_k] != 0) or i_n == i_k:
        break
    current = que.popleft()
    for i in [current - 1, current + 1, current * 2]:
        if (0 <= i <= 100000) and visited[i] == 0:
            visited[i] = visited[current] + 1
            que.append(i)
print(visited[i_k])