# 브루트포스
import sys

i_n, i_m = map(int, sys.stdin.readline().split())
ls_nm = [list(map(int, sys.stdin.readline().split())) for _ in range(i_n)]
# 폴리오미노 전체 경우의 수
ls_tetris = [
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (1, 0), (0, 1), (1, 1)),
    ((0, 0), (1, 0), (2, 0), (0, 1)),
    ((0, 0), (-1, 0), (0, 1), (0, 2)),
    ((-2, 0), (-1, 0), (0, 0), (0, -1)),
    ((0, 0), (0, -1), (0, -2), (1, 0)),
    ((0, 0), (0, -1), (1, 0), (2, 0)),
    ((0, 0), (0, 1), (0, 2), (1, 0)),
    ((0, 0), (-1, 0), (-2, 0), (0, 1)),
    ((0, 0), (-1, 0), (0, -1), (0, -2)),
    ((0, 0), (1, 0), (1, -1), (2, -1)),
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    ((0, 0), (0, 1), (-1, 1), (-1, 2)),
    ((0, 0), (1, 0), (1, -1), (2, 0)),
    ((0, 0), (0, 1), (1, 1), (0, 2)),
    ((0, 0), (-1, 0), (-1, 1), (-2, 0)),
    ((0, 0), (0, -1), (-1, -1), (0, -2))
]
tetris_sum_max = 0
for y in range(i_n):
    for x in range(i_m):
        for tetris in ls_tetris:
            tetris_sum = 0
            for n in range(4):
                nx = x + tetris[n][0]
                ny = y + tetris[n][1]
                # 잘리는 경우는 결국 최댓값 안에 포함되어 따로 처리 안함
                if 0 <= nx < i_m and 0 <= ny < i_n:
                    tetris_sum += ls_nm[ny][nx]
                else: 
                    break
            if tetris_sum > tetris_sum_max:
                tetris_sum_max = tetris_sum
print(tetris_sum_max)
