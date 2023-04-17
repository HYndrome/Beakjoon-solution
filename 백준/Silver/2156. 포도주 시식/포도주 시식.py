import sys
i_n = int(sys.stdin.readline())
ls_wine = [int(sys.stdin.readline()) for i in range(i_n)]

if i_n == 1:
    print(ls_wine[-1])
elif i_n == 2:
    print(ls_wine[0] + ls_wine[1])
else:
    ls_max_wine = [0] * (i_n)
    ls_max_wine[0] = ls_wine[0]
    ls_max_wine[1] = ls_wine[0] + ls_wine[1]
    ls_max_wine[2] = max(ls_wine[0] + ls_wine[1], ls_wine[1] + ls_wine[2], ls_wine[0] + ls_wine[2])
    for i in range(2, i_n-1):
        ls_max_wine[i+1] = max(ls_max_wine[i-2] + ls_wine[i] + ls_wine[i+1], ls_max_wine[i-1] + ls_wine[i+1], ls_max_wine[i])
    print(ls_max_wine[-1])