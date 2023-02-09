import sys
i_n = int(sys.stdin.readline())
stk_out = []
for i_1 in range(i_n):
    ls_in = tuple(sys.stdin.readline().split())
    if ls_in[0] == 'push':
        stk_out.append(ls_in[1])
    elif ls_in[0] == 'pop':
        if stk_out:
            print(stk_out.pop())
        else:
            print(-1)
    elif ls_in[0] == 'size':
        print(len(stk_out))
    elif ls_in[0] == 'empty':
        if stk_out:
            print(0)
        else:
            print(1)
    elif ls_in[0] == 'top':
        if stk_out:
            print(stk_out[-1])
        else:
            print(-1)