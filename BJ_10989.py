import sys

i_n = int(sys.stdin.readline())
lst_0 = [0 for i_1 in range(10000)]
for i_2 in range(i_n):
    i_n1 = int(sys.stdin.readline())
    lst_0[i_n1 -1] += 1
for i_3 in range(10000):
    if lst_0[i_3] != 0:
        for i_4 in range(lst_0[i_3]):
            print(i_3+1)