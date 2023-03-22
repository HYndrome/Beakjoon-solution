import sys
i_n = int(sys.stdin.readline())
ls_compare = [int(sys.stdin.readline()) for i_1 in range(i_n)]
# stack 1 2 3 4 ++++
# ls
# stack 1 2 --
# ls 4 3
# stack 1 2 5 6 ++
# ls 4 3
# stack 1 2 5 -
# ls 4 3 6
# stack 1 2 7 8 ++
# ls 4 3 6
# stack  -----
# ls 4 3 7 8 7 2 1
ls_magazine = [i_2 for i_2 in range(i_n, 0, -1)]
i_p = 0
ls_stack = []
ls_input = []
ls_cal = []
while (ls_magazine) or (ls_stack) :
    if not ls_stack:
        ls_stack.append(ls_magazine.pop())
        ls_cal.append('+')
    else:
        if ls_stack[-1] == ls_compare[i_p]:
            ls_input.append(ls_stack.pop())
            i_p += 1
            ls_cal.append('-')
        elif ls_stack[-1] != ls_compare[i_p]:
            try:
                ls_stack.append(ls_magazine.pop())
                ls_cal.append('+')
            except IndexError:
                print('NO')
                break
else:
    for s_1 in ls_cal:
        print(s_1)