import sys


i_t = int(sys.stdin.readline())

for case in range(i_t):
    i_n = int(sys.stdin.readline())
    set_n = set(map(int, sys.stdin.readline().split()))
    i_m = int(sys.stdin.readline())
    ls_m = list(map(int, sys.stdin.readline().split()))
    for i in ls_m:
        if i in set_n:
            print(1)
        else:
            print(0)