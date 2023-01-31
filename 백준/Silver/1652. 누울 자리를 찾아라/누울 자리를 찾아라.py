i_n = int(input())
mtrx_input = [list(input()) for i_1 in range(i_n)]
i_output_m = 0
i_output_n = 0
for i_2 in range(i_n):
    bool_connection_row = True
    for i_3 in range(i_n - 1):
        if (mtrx_input[i_2][i_3] == '.') * (mtrx_input[i_2][i_3 + 1] == '.') * (bool_connection_row):
            i_output_m += 1
            bool_connection_row = False
        elif (mtrx_input[i_2][i_3] != '.'):
            bool_connection_row= True
for i_4 in range(i_n):
    bool_connection_col = True
    for i_5 in range(i_n - 1):
        if (mtrx_input[i_5][i_4] == '.') * (mtrx_input[i_5 + 1][i_4] == '.') * (bool_connection_col):
            i_output_n += 1
            bool_connection_col = False
        elif (mtrx_input[i_5][i_4] != '.'):
            bool_connection_col = True
print(i_output_m, i_output_n)