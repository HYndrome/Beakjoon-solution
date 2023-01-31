for i_1 in range(int(input())):
    i_m, i_n = map(int, input().split())
    matrix_input = [list(map(int,(input().split()))) for i_2 in range(i_m)]
    matrix_rotate = [[0]*i_m for i_2 in range(i_n)]
    matrix_zero = [[0]*i_m for i_2 in range(i_n)]
    i_distance = 0
    for i_3 in range(i_m):
        for i_4 in range(i_n):
            matrix_rotate[i_4][i_m - i_3 - 1] = matrix_input[i_3][i_4]
    for i_5 in range(i_n):
        i_move = 0 
        for i_6 in range(i_m):
            if matrix_rotate[i_5][i_6] == 1:
                i_distance += i_6 - i_move
                i_move += 1
    print(i_distance)