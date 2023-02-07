import sys

i_n = int(sys.stdin.readline())
lst_stack = []
for i_1 in range(i_n):
    lst_stack.append(int(sys.stdin.readline()))
i_max = 0
i_cnt = 0
for i_1 in reversed(lst_stack):
    if i_1 > i_max:
        i_cnt += 1
        i_max = i_1
print(i_cnt)