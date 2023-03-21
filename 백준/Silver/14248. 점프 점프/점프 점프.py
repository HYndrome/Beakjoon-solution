from collections import deque
i_n = int(input())
ls_n = list(map(int, input().split()))
i_s = int(input()) - 1

graph = [[] for i_1 in range(i_n)]
for i_2 in range(i_n):
    graph[i_2].append(i_2 - ls_n[i_2])
    graph[i_2].append(i_2 + ls_n[i_2])

ls_visited = [False] * i_n

que = deque()
que.append(i_s)
ls_visited[i_s] = True
while que:
    v = que.popleft()
    for i_3 in graph[v]:
        if 0 <= i_3 < i_n:
            if ls_visited[i_3] == False:
                ls_visited[i_3] = True
                que.append(i_3)

print(ls_visited.count(True))