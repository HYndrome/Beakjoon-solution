import sys

i_n = int(sys.stdin.readline())

lst_2m = [0 for i_1 in range(2000001)]

for i_2 in range(i_n):
    i_n1 = int(sys.stdin.readline())
    lst_2m[i_n1 + 1000000] = 1

for i_3 in range(2000001):
    if lst_2m[i_3] == True:
        print(i_3 - 1000000)