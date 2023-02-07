dct_move = {
    'LT': (-1, -1), 'T': (0, -1), 'RT': (1, -1),
    'L': (-1, 0), 'R': (1, 0),
    'LB': (-1, 1), 'B': (0, 1), 'RB': (1, 1)
}
lst_chess = [[0]*8 for i_1 in range(8)]
dct_col = {
    '8': 0, '7': 1, '6': 2, '5': 3,
    '4': 4,  '3': 5, '2': 6 , '1': 7 
    }
dct_row = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4,  'F': 5, 'G': 6 , 'H': 7 
    }

s_index_k, s_index_s, s_move = input().split()
lst_move_his = []
for i_1 in range(int(s_move)):
    lst_move_his.append(input())

x_k = dct_row[s_index_k[0]]
y_k = dct_col[s_index_k[1]]
x_s = dct_row[s_index_s[0]]
y_s = dct_col[s_index_s[1]]

for s_1 in lst_move_his:
    x_k += dct_move[s_1][0]
    y_k += dct_move[s_1][1]
    if (x_k < 0) + (x_k > 7) + (y_k < 0) + (y_k > 7):
        x_k -= dct_move[s_1][0]
        y_k -= dct_move[s_1][1]
        
    if (x_k == x_s) * (y_k == y_s):
        x_s += dct_move[s_1][0]
        y_s += dct_move[s_1][1]
    if (x_s < 0) + (x_s > 7) + (y_s < 0) + (y_s > 7):
        x_k -= dct_move[s_1][0]
        y_k -= dct_move[s_1][1]
        x_s -= dct_move[s_1][0]
        y_s -= dct_move[s_1][1]

k_final_x = [key_1 for key_1, value_1 in dct_row.items() if value_1 == x_k]
k_final_y = [key_2 for key_2, value_2 in dct_col.items() if value_2 == y_k]
s_final_x = [key_3 for key_3, value_3 in dct_row.items() if value_3 == x_s]
s_final_y = [key_4 for key_4, value_4 in dct_col.items() if value_4 == y_s]
print(*k_final_x, *k_final_y, sep= '')
print(*s_final_x, *s_final_y, sep= '')