import sys

i_n = int(sys.stdin.readline())
lst_letter = []
for i_1 in range(i_n):
    s_n = sys.stdin.readline().rstrip()
    lst_letter.append(s_n)
lst_letter = list(set(lst_letter))
lst_letter.sort(key= lambda x: (len(x), x))
print(*lst_letter, sep='\n')