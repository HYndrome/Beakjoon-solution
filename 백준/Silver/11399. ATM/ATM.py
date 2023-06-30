i_n = int(input())
ls_p = list(map(int, input().split()))
ls_p.sort(reverse=True)
cnt = len(ls_p)
sum_p = 0
while ls_p:
    current_min = ls_p.pop()
    sum_p += current_min * cnt
    cnt -= 1
print(sum_p)