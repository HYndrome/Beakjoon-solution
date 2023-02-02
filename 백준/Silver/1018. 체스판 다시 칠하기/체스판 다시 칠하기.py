import sys

i_n, i_m = map(int, input().split())
lst_input = [input() for i_1 in range(i_n)]

l_w = [s_1 for s_1 in 'WBWBWBWB']
l_b = [s_2 for s_2 in 'BWBWBWBW']
lst_chess_1 = [l_w, l_b, l_w, l_b, l_w, l_b, l_w, l_b]
lst_chess_2 = [l_b, l_w, l_b, l_w, l_b, l_w, l_b, l_w]

i_chess_final = 64
for i_2 in range(i_n - 7):
    for i_3 in range(i_m - 7):
        i_chess_1 = 0
        i_chess_2 = 0
        for i_4 in range(8):
            for i_5 in range(8):
                if lst_input[i_2 + i_4][i_3 + i_5] == lst_chess_1[i_4][i_5]:
                    pass
                else:
                    i_chess_1 += 1
                if lst_input[i_2 + i_4][i_3 + i_5] == lst_chess_2[i_4][i_5]:
                    pass
                else:
                    i_chess_2 += 1    
        if i_chess_1 < i_chess_final:
            i_chess_final = i_chess_1
        if i_chess_2 < i_chess_final:
            i_chess_final = i_chess_2
            
print(i_chess_final)