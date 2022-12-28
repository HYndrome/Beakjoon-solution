import sys

i_n, i_k = map(int, sys.stdin.readline().split())
lst_score = list(map(int,sys.stdin.readline().split()))
lst_score.sort(reverse = True)
print(lst_score[i_k-1])