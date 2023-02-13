i_x, i_y, i_m, i_n = map(int, input().split())
print(min(i_x, i_m - i_x, i_y, i_n - i_y))