H, M = map(int, input().split())
total_M = 60*H+M-45
print(total_M//60%24,total_M%60)