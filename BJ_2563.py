import sys

matrix_0 = [list(0 for i_1 in range(100)) for i_2 in range(100)]

def colorpaper(x, y):
    for i_3 in matrix_0[y-1 : y+9]:
        for i_4 in range(x-1, x+9):
            i_3[i_4] = 1

i_5 = int(sys.stdin.readline())

for i_6 in range(i_5):
    x_1, y_1 = map(int, sys.stdin.readline().split())
    colorpaper(x_1, y_1)

count_1 = 0

for i_7 in matrix_0:
    for i_8 in i_7:
        if i_8 == 1:
            count_1 += 1

print(count_1)