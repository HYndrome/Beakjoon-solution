import sys

i_n, i_m = map(int, input().split())
set_a = set()
set_a.update([sys.stdin.readline().rstrip() for i_1 in range(i_n)])
lst_b = [sys.stdin.readline().rstrip() for i_2 in range(i_m)]

i_result = 0
for s_1 in lst_b:
    if s_1 in set_a:
        i_result += 1
print(i_result)