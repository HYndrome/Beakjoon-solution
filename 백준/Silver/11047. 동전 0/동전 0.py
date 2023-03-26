import sys

i_n, i_k = map(int, sys.stdin.readline().split())
ls_coin = [int(sys.stdin.readline()) for i_1 in range(i_n)]
cnt_coin = 0

for i_2 in reversed(ls_coin):
    cnt_coin += i_k // i_2
    i_k %= i_2

print(cnt_coin) 