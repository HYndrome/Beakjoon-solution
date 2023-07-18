# bfs 최단거리 풀이 - 어림도 없지 시간 초
from collections import deque

# 입력
i_n = int(input())
# 방문처리 
visited = [0] * (i_n + 1)
# 제곱 수 구하기
ls_square = []
num_index = 1
while True:
    num_square = num_index ** 2
    ls_square.append(num_square)
    if num_square >= i_n:
        break
    num_index += 1
ls_square = list(reversed(ls_square))

que = deque([0])
while que:
    current = que.popleft()
    if current == i_n:
        break
    for square in ls_square:
        next_point = current + square
        if next_point <= i_n and visited[next_point] == 0:
            visited[next_point] = visited[current] + 1
            que.append(next_point)
        if next_point == i_n:
            break
print(visited[i_n])