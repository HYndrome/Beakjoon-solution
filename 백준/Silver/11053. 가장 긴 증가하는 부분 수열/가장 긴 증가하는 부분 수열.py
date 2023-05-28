i_n = int(input())
ls_a = list(map(int, input().split()))
dp = [(0, 0) for _ in range(i_n)]
dp[0] = (ls_a[0], 1)

for i in range(1, i_n):
    cnt = 0
    for j in range(0, i):
        if ls_a[i] > dp[j][0]:
            if cnt < dp[j][1]:
                cnt = dp[j][1]
    dp[i] = (ls_a[i], cnt + 1)

v_max = max(dp, key= lambda x: x[1])
print(max(dp, key= lambda x: x[1])[1])