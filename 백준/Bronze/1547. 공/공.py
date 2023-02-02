i_m = int(input())
lst_ball = [1, 0, 0]
for i_1 in range(i_m):
    i_mix_1, i_mix_2 = map(int, input().split())
    lst_ball[i_mix_1 - 1], lst_ball[i_mix_2 - 1] = lst_ball[i_mix_2 - 1], lst_ball[i_mix_1 - 1]
print(lst_ball.index(1) + 1) 