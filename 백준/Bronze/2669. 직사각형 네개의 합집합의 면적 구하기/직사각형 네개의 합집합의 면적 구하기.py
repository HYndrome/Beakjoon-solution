mtrx_blank = [[0 for i_1 in range(100)] for i_2 in range(100)]
i_sum = 0
for i_3 in range(4):
    i_x1, i_y1, i_x2, i_y2 = map(int, input().split())
    for i_4 in range(i_y1, i_y2):
        mtrx_blank[i_4][i_x1:i_x2] = [1]*(i_x2 - i_x1)
for i_5 in range(len(mtrx_blank)):
    i_sum += sum(mtrx_blank[i_5])
print(i_sum)