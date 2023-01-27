import sys

i_n = int(sys.stdin.readline())
set_word = set(sys.stdin.readline().rstrip() for i_1 in range(i_n))
lst_word = sorted(set_word, key= lambda x: (len(x), x))
print(*lst_word, sep= '\n')