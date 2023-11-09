# bfs 최단거리, 델타 탐색

from collections import deque

def solution(board):
    # 그래프 입력, 시작점-끝점 좌표 구하기
    graph = []
    start = []
    end = []
    index_row = 0
    index_col = 0
    L_row = len(board[0])
    L_col = len(board)
    for row in board:
        row_new = []
        for s_row in row:
            if s_row == ".":
                row_new.append(0)
            elif s_row == "D":
                row_new.append(-1)
            elif s_row == "R":
                row_new.append(0)
                start = [index_row, index_col]
            elif s_row == "G":
                row_new.append(0)
                end = [index_row, index_col]
            index_row += 1
        graph.append(row_new)
        index_col += 1
        index_row = 0
    # 시작점에서 그래프 탐색
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    que = deque([])
    que.append(start)
    # bfs 탐색
    while que:
        x_current, y_current = que.popleft()
        for i in range(4):
            nx = x_current + delta[i][0]
            ny = y_current + delta[i][1]
            # 바로 앞에 막혀있는 경우 처리
            if 0 <= nx < L_row and 0 <= ny < L_col: 
                if graph[ny][nx] == -1:
                    continue
            # 맨 끝에 부딪힐 때까지 미끄러저 이동 구현
            while True:
                if (nx <= 0 or nx >= L_row - 1) and delta[i][0] != 0:
                    print(nx, ny, "a")
                    break
                if (ny <= 0 or ny >= L_col - 1) and delta[i][1] != 0:
                    print(nx, ny, "b")
                    break
                if 0 <= nx + delta[i][0] < L_row and 0 <= ny + delta[i][1] < L_col:
                    if graph[ny + delta[i][1]][nx + delta[i][0]] == -1:
                        print(nx, ny, "c")
                        break
                nx += delta[i][0]
                ny += delta[i][1]
            if 0 <= nx < L_row and 0 <= ny < L_col:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y_current][x_current] + 1
                    if ny == 4 and nx == 4:
                        print("===========")
                        print(graph[y_current][x_current], x_current, y_current)
                    que.append([nx, ny])
                    if nx == end[0] and ny == end[1]:
                        break
    # 목표위치 출력
    answer = 0
    if graph[end[1]][end[0]] == 0:
        answer = -1
    else:
        answer = graph[end[1]][end[0]]
    return answer