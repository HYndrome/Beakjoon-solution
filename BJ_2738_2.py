import sys

i_n, i_m = map(int, sys.stdin.readline().split())

matrix_1 = [list(map(int, sys.stdin.readline().split())) for i_1 in range(i_n)]
matrix_2 = [list(map(int, sys.stdin.readline().split())) for i_2 in range(i_n)]

for i_3, i_4 in zip(matrix_1, matrix_2):
    print(*list(i_5 + i_6 for i_5, i_6 in zip(i_3, i_4)))