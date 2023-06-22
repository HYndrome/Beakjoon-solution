i_n, i_r, i_c = map(int, input().split())
answer = 0
num_sub = 2 ** (i_n - 1)
def calutelate_z(row, col):
    global answer
    if row < 2 and col < 2:
        if row == 0 and col == 0:
            return
        elif row== 1 and col == 0:
            answer += 2
        elif row == 0 and col == 1:
            answer += 1
        else:
            answer += 3
    else:
        global num_sub
        if row >= num_sub:
            answer += 2 * (num_sub ** 2)
            row -= num_sub
        if col >= num_sub:
            answer += num_sub ** 2
            col -= num_sub
        num_sub //= 2
        calutelate_z(row, col)
    return
calutelate_z(i_r, i_c)
print(answer)
