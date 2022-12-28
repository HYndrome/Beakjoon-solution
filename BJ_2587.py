import sys

lst_1 = []
sum = 0
for i_1 in range(5):
    i_2 = int(sys.stdin.readline())
    lst_1.append(i_2)
    sum += i_2
print(f'{sum/5:.0f}')
lst_1.sort()
print(lst_1[2])