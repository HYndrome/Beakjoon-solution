mtrx_input = []
for i_1 in range(5):
    mtrx_input.append(list(input()))
s_output = ''
for i_i in range(max(map(len, mtrx_input))):
    for i_j in range(5):
        try:
            s_output += mtrx_input[i_j][i_i]
        except IndexError:
            continue
print(s_output)