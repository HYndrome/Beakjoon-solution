from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 바깥 경로 그리기 -3 직사각형 내부 -2  / 직사각형 경계선 -1
    graph = [[-3] * 101 for _ in range(101)]
    for rect in rectangle:
        for y_rect in range(2*rect[1], 2*rect[3]+1, 1):
            for x_rect in range(2*rect[0], 2*rect[2]+1, 1):
                # 경계선 처리
                if y_rect == 2*rect[1] or y_rect == 2*rect[3] or x_rect == 2*rect[0] or x_rect == 2*rect[2]:
                    if graph[y_rect][x_rect] != -2:
                        graph[y_rect][x_rect] = -1
                # 내부 처리        
                else:
                    graph[y_rect][x_rect] = -2
                    
    # 최단거리 bfs - deque
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    def bfs(x, y):
        graph[y][x] = 0
        que = deque([])
        que.append((x, y))
        while que:
            x, y = que.popleft()
            if x == 2*itemX and y == 2*itemY:
                break
            for d in delta:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < 101 and 0 <= ny < 101:
                    if graph[ny][nx] == -1:
                        que.append((nx, ny))
                        graph[ny][nx] = graph[y][x] + 1

    bfs(2*characterX, 2*characterY)
    answer = graph[2*itemY][2*itemX]
    return answer // 2