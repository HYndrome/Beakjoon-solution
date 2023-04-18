import sys
from collections import deque

i_m, i_n, i_h = map(int, sys.stdin.readline().split())
ls_tomato = []
ls_record = []
que_tomato = deque()
for z in range(i_h):
    ls_tomato_xy = []
    ls_record_xy = []
    for y in range(i_n):
        ls_tomato_x = []
        ls_record_x = []
        ls_input = list(map(int, sys.stdin.readline().split()))
        for x in range(i_m):
            ls_tomato_x.append(ls_input[x])
            if ls_input[x] == -1:
                ls_record_x.append(-1)
            elif ls_input[x] == 0:
                ls_record_x.append(0)
            elif ls_input[x] == 1:
                ls_record_x.append(1)
                que_tomato.append((x,y,z))
        ls_tomato_xy.append(ls_tomato_x)
        ls_record_xy.append(ls_record_x)
    ls_tomato.append(ls_tomato_xy)
    ls_record.append(ls_record_xy)

delta = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

while que_tomato:
    tomato = que_tomato.popleft()
    for i in range(6):
        nx = tomato[0] + delta[i][0]
        ny = tomato[1] + delta[i][1]
        nz = tomato[2] + delta[i][2]
        if (0 <= nx < i_m) and (0 <= ny < i_n) and (0 <= nz < i_h):
            if ls_record[nz][ny][nx] == 0:
                ls_record[nz][ny][nx] = ls_record[tomato[2]][tomato[1]][tomato[0]] + 1
                que_tomato.append((nx, ny, nz))

tomato_max = 1
bool_break = False
for z in range(i_h):
    for y in range(i_n):
        for x in range(i_m):
            if ls_record[z][y][x] == 0:
                bool_break = True
            elif ls_record[z][y][x] > tomato_max:
                tomato_max = ls_record[z][y][x]

if bool_break == True:
    print(-1)
else:
    print(tomato_max - 1)