from collections import deque

i_t = int(input())
for i_1 in range(i_t):
    i_n, i_m = map(int, input().split())
    s_input = input().split()
    ls_input = []
    for i_2 in range(i_n):
        ls_input.append((int(s_input[i_2]), i_2))
    dq_input = deque(ls_input)
    i_cnt = 1
    while True:
        if dq_input[0][0] < max(dq_input)[0]:
            dq_input.rotate(-1)
        else:
            i_pop = dq_input.popleft()
            if i_pop[1] == i_m:
                break
            i_cnt += 1
    print(i_cnt)