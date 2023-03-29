i_n, i_m = map(int, input().split())
i_j = int(input())
p_basket = 1
cnt_move = 0
for i_2 in range(i_j):
    p_apple = int(input())
    if p_apple < p_basket:
        cnt_move += (p_basket - p_apple)
        p_basket = p_apple
    elif p_apple > p_basket + (i_m - 1):
        cnt_move += p_apple - (p_basket + (i_m - 1))
        p_basket = p_apple - (i_m - 1)
print(cnt_move)