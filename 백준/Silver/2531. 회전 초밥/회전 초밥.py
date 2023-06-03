import sys
i_n, i_d, i_k, i_c = map(int, sys.stdin.readline().split())
ls_sushi = [int(sys.stdin.readline()) for _ in range(i_n)]
cnt_max = 0
for start in range(len(ls_sushi)):
    set_sushi = set([ls_sushi[i] for i in range(start, start - i_k, -1)])
    cnt_current = len(set_sushi)
    if i_c not in set_sushi:
        cnt_current += 1
    if cnt_current > cnt_max:
        cnt_max = cnt_current
print(cnt_max)