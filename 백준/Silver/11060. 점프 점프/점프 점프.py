from collections import deque

i_n = int(input())
graph = []
graph.append([])
ls_input =list(map(int, input().split()))
for i_1 in range(len(ls_input)):
    if ls_input[i_1] == 0:
        graph.append([])
    else:
        graph.append(list(range(i_1 + 2, i_1 + 2 + ls_input[i_1])))

visited = [-1] * (i_n + 1)
result = []

def jump(start, end):
    que = deque([start])
    visited[start] = 0
    while que:
        v = que.popleft()
        if v <= end:
            for i_2 in graph[v]:
                if i_2 <= end:
                    if visited[i_2] == -1:
                        que.append(i_2)
                        visited[i_2] = visited[v] + 1
        if visited[end] != -1:
            break
    return visited[end]

print(jump(1, i_n))