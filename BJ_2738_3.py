import numpy as np
import sys

i_n, i_m = map(int, sys.stdin.readline().split())
matrix_1 = np.array([list(map(int, sys.stdin.readline().split())) for i_1 in range(i_n)])
matrix_2 = np.array([list(map(int, sys.stdin.readline().split())) for i_2 in range(i_n)])
matrix_sum = matrix_1 + matrix_2
for i_3 in range(i_n):
    print(*matrix_sum[i_3])