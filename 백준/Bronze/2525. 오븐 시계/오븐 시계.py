i_h, i_m = map(int, input().split())
i_cook = int(input())
i_total = i_h * 60 + i_m + i_cook
print(i_total//60%24, i_total%60)