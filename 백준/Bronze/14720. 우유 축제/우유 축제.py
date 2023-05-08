i_n = int(input())
cnt = 0
for i in map(int, input().split()):
    if i == cnt % 3:
        cnt += 1
print(cnt)