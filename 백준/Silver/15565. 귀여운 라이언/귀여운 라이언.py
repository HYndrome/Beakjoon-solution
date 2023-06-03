i_n, i_k = map(int, input().split())
ls_doll = list(map(int, input().split()))
ls_ryanIndex = [i for i in range(len(ls_doll)) if ls_doll[i] == 1]
if len(ls_ryanIndex) < i_k:
    print('-1')
else:
    cnt_min = 1e6
    start = 0
    while start <= len(ls_ryanIndex) - i_k:
        end = start + i_k - 1
        cnt_current = ls_ryanIndex[end] - ls_ryanIndex[start] + 1
        if cnt_current < cnt_min:
            cnt_min = cnt_current
        start += 1
    print(cnt_min)