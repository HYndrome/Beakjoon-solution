import sys

i_n = int(sys.stdin.readline())
# 밑에서 dp[i-3] 인덱싱 때문에 편의로 [0]을 하나 더 추가
ls_stair = [0] + [int(sys.stdin.readline()) for i in range(i_n)] + [0]

dp = [0] * (i_n + 2)
dp[1] = ls_stair[1]
dp[2] = dp[1] + ls_stair[2]

for i in range(3, i_n+1):
    # i번째 계단을 1칸 건너서 올라온 경우 vs 바로 올라온 경우
    dp[i] = max(dp[i-2], dp[i-3] + ls_stair[i-1]) + ls_stair[i]

print(dp[i_n])