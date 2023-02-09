from collections import deque
import sys

i_n = int(sys.stdin.readline())
que_out = deque()
for i_1 in range(i_n):
    tp_in = tuple(sys.stdin.readline().split())
    if tp_in[0] == 'push':
        que_out.append(int(tp_in[1]))
    elif tp_in[0] == 'pop':
        if que_out:
            print(que_out.popleft())
        else:
            print(-1)
    elif tp_in[0] == 'size':
        print(len(que_out))
    elif tp_in[0] == 'empty':
        if que_out:
            print(0)
        else:
            print(1)
    elif tp_in[0] == 'front':
        if que_out:
            print(que_out[0])
        else:
            print(-1)
    elif tp_in[0] == 'back':
        if que_out:
            print(que_out[-1])
        else:
            print(-1)