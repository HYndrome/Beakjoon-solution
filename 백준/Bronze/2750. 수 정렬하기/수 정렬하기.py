import sys

i_1 = int(sys.stdin.readline())
lst_1 = []

for i_2 in range(i_1):
    i_3 = int(sys.stdin.readline())
    lst_1.append(i_3)
for i_4 in range(i_1):
    i_min = min(lst_1)
    print(i_min)
    lst_1.remove(i_min)