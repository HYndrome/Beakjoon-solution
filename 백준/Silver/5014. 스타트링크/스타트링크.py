from collections import deque

i_f, i_s, i_g, i_u, i_d = map(int, input().split())

ls_visited =  [-1] * (i_f + 1)
ls_visited[i_s] = 0
que = deque()
que.append(i_s)
while que:
    v_floor = que.popleft()
    if (v_floor + i_u <= i_f):
        if ls_visited[v_floor + i_u] == -1:
            ls_visited[v_floor + i_u] = ls_visited[v_floor] + 1
            que.append(v_floor + i_u)
    if v_floor - i_d >= 1:
        if ls_visited[v_floor - i_d] == -1:
            ls_visited[v_floor - i_d] = ls_visited[v_floor] + 1
            que.append(v_floor - i_d)
    if ls_visited[i_g] != -1:
        print(ls_visited[i_g])
        break
if ls_visited[i_g] == -1:
    print('use the stairs')