import sys
from collections import deque

i_row, i_col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i_1 in range(i_row)]

dx = [1, 1, 1, 0,-1, -1, -1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]
cnt_char = 0

for i_2 in range(i_row):
    for i_3 in range(i_col):
        if graph[i_2][i_3] == 0:
            continue
        else:
            graph[i_2][i_3] = 0
            que = deque()
            que.append((i_3, i_2))
            while que:
                x, y = que.popleft()
                for i_4 in range(8):
                    nx = x + dx[i_4]
                    ny = y + dy[i_4]
                    if (nx < 0) + (nx >= i_col) + (ny < 0) + (ny >= i_row):
                        continue
                    elif graph[ny][nx] == 1:
                        que.append((nx, ny))
                        graph[ny][nx] = 0
            cnt_char += 1

print(cnt_char)