# 각 케이스마다 합을 구하는 것은 연산 낭비라서 dp로 계산 결과 저장
import sys

# 입력값 받기
i_n, i_m = map(int, sys.stdin.readline().split())
ls_n = list(map(int, sys.stdin.readline().split()))
# dp 빈리스트 형성 ls_sum[0] = 0이고 결과 값을 ls_sum[1]부터 작성
ls_sum = [0] * (i_n + 1)
# 처음부터 i까지의 합을 ls_sum[i + 1]에 저장
ls_sum[1] = ls_n[0]
for i in range(2, i_n + 1):
    ls_sum[i] = ls_sum[i - 1] + ls_n[i - 1]
# 각 케이스별로 계산 결과 값 출력
for case_m in range(i_m):
    start, end = map(int, sys.stdin.readline().split())
    sum_m = ls_sum[end] - ls_sum[start - 1]
    print(sum_m)