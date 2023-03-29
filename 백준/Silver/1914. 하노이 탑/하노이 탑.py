i_n = int(input())

ls_stack = []
def hanoi_stack(stack, start, end):
    if stack == 1:
        ls_stack.append((start, end))
    else:
        left = [i_1 for i_1 in [1, 2, 3] if (i_1 != start) and (i_1 != end)].pop()
        hanoi_stack(stack - 1, start, left)
        hanoi_stack(1, start, end)
        hanoi_stack(stack - 1, left, end)


def hanoi_cnt(stack):
    if stack == 1:
        return 1
    else:
        return hanoi_cnt(1) + 2 *hanoi_cnt(stack - 1)

if i_n <= 20:
    hanoi_stack(i_n, 1, 3)
    print(len(ls_stack))
    for tup_1 in ls_stack:
        print(*tup_1)
else:
    cnt = 0
    cnt += hanoi_cnt(i_n)
    print(cnt)