import sys

i_k = int(sys.stdin.readline())
lst_int = []
for i_1 in range(i_k):
    i_int = int(sys.stdin.readline())
    if i_int == 0:
        try:
            lst_int.pop()
        except IndexError:
            lst_int.append(0)
    else:
        lst_int.append(i_int)
print(sum(lst_int))