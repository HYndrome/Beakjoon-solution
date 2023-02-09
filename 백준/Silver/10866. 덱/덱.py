from collections import deque
import sys

i_n = int(sys.stdin.readline())
dq_out = deque()
for i_1 in range(i_n):
    tup_in = tuple(sys.stdin.readline().split())
    if tup_in[0] == 'push_front':
        dq_out.appendleft(tup_in[1])
    elif tup_in[0] == 'push_back':
        dq_out.append(tup_in[1])
    elif tup_in[0] == 'pop_front':
        if dq_out:
            print(dq_out.popleft())
        else:
            print(-1)
    elif tup_in[0] == 'pop_back':
        if dq_out:
            print(dq_out.pop())
        else:
            print(-1)
    elif tup_in[0] == 'size':
        print(len(dq_out))
    elif tup_in[0] == 'empty':
        if dq_out:
            print(0)
        else:
            print(1)
    elif tup_in[0] == 'front':
        if dq_out:
            print(dq_out[0])
        else:
            print(-1)
    elif tup_in[0] == 'back':
        if dq_out:
            print(dq_out[-1])
        else:
            print(-1)