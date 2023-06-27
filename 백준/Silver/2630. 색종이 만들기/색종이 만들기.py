import sys

i_n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(i_n)]
cnt_white = 0
cnt_blue = 0
def paper_cutter(x, y, size):
    global cnt_white
    global cnt_blue
    conformity = True
    color_start = graph[y][x]
    # 색상 일치 확인
    for ny in range(y, y + size):
        for nx in range(x, x + size):
            if graph[ny][nx] != color_start:
                conformity = False
                break
        if conformity == False:
            break
    # 일치에 따른 처리
    if conformity == True:
        if color_start == 0:
            cnt_white += 1
        else:
            cnt_blue += 1
    else:
        paper_cutter(x, y, size // 2)
        paper_cutter(x + size // 2, y, size // 2)
        paper_cutter(x, y + size // 2, size // 2)
        paper_cutter(x + size // 2 , y + size // 2, size // 2)

paper_cutter(0, 0, i_n)
print(cnt_white)
print(cnt_blue)