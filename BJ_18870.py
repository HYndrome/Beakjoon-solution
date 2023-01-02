import sys

i_n = int(sys.stdin.readline())
lst_i = list(map(int, sys.stdin.readline().split()))
set_i = set(lst_i)
lst_i2 = list(set_i)
lst_i2.sort()
for i_1 in lst_i:
    print(lst_i2.index(i_1), end = " ")

# set 자료형은 순서가 없어서 인덱스가 없다.
# 시간 초과