import sys


i_n = int(sys.stdin.readline())
# 문제에서 입력 받는 수는 1000000보다 절댓값이 작거나 같은 정수
ls_number = [0] * 2000001
for i in range(i_n):
    ls_number[int(sys.stdin.readline()) + 1000000] = 1
for i in range(2000001):
    if ls_number[i]:
        print(i - 1000000)
