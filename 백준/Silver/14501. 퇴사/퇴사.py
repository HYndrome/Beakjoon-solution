i_n = int(input())

consulting = [tuple(map(int, input().split())) for _ in range(i_n)]

dp = [0] * (i_n + 1)

for i in range(i_n):
    for j in range(i + consulting[i][0], i_n + 1):
        if dp[j] < dp[i] + consulting[i][1]:
            dp[j] = dp[i] + consulting[i][1]
            # print(dp)

print(dp[-1])