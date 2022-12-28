import sys

i_n = int(sys.stdin.readline())
lst_0 = []
for i_1 in range(i_n):
    i_n1 = int(sys.stdin.readline())
    lst_0.append(i_n1)
lst_0.sort()
for i_2 in range(len(lst_0)):
    print(lst_0[i_2])