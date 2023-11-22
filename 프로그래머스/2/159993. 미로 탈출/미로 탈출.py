# bfs 최단거리
from collections import deque

def bfs(maps, start, end):
    """탐색해야하는 맵과 시작지점[a, b]과 끝지점[c, d]을 받아서 최소로 이동해야하는 거리를 return하는 함수, 도달할 수 없는 경우 -1 return"""
    len_y = len(maps)
    len_x = len(maps[0])
    visited = [[0] * len_x for _ in range(len_y)]
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    que = deque()
    que.append(start)
    while que:
        x, y = que.popleft()
        if [x, y] == end:
            return visited[y][x]
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < len_x and 0 <= ny < len_y:
                if maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append([nx, ny])                
    return -1

def solution(maps):
    answer = 0
    # 시작점, 레버위치, 종료점 인덱스 찾기
    len_y = len(maps)
    len_x = len(maps[0])
    p_start = [-1, -1]
    p_lever = [-1, -1]
    p_end = [-1, -1]
    for y in range(len_y):
        for x in range(len_x):
            if maps[y][x] == 'S':
                p_start = [x, y]
            if maps[y][x] == 'L':
                p_lever = [x, y]
            if maps[y][x] == 'E':
                p_end = [x, y]
    # bfs 델타 탐색 - 시작부터 레버까지
    move_s_to_l = bfs(maps, p_start, p_lever)
    if move_s_to_l == -1:
        return -1
    else:
        move_l_to_e = bfs(maps, p_lever, p_end)
        if move_l_to_e == -1:
            return -1
        else:
            answer = move_s_to_l + move_l_to_e
    return answer