i_n, i_k = map(int, input().split())
ls_coin = [int(input()) for _ in range(i_n)]

dp = [10001] * (i_k + 1)
dp[0] = 0

for coin in ls_coin:
    for i in range(coin, i_k + 1):
        dp[i] = min(dp[i], dp[i-coin] + 1)


if dp[i_k] == 10001:
    print(-1)
else:
    print(dp[i_k])