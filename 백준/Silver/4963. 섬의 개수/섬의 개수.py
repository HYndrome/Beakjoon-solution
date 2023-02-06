import sys
sys.setrecursionlimit(10**6)
def island_checker(graph, x, y):
    if graph[y][x] == 1:
        graph[y][x] = 0
        delta_x = [-1, 0, 1, -1, 1, -1, 0, 1]
        delta_y = [1, 1, 1, 0, 0, -1, -1, -1]
        for i_1 in range(8):
            x_new = x + delta_x[i_1]
            y_new = y + delta_y[i_1]
            if (x_new >= 0) * (x_new <= i_w - 1) * (y_new >= 0) * (y_new <= i_h - 1):
                island_checker(graph, x_new, y_new)
while True:
    i_w, i_h = map(int, sys.stdin.readline().split())
    if (i_w == 0) * (i_h == 0):
        break
    else:
        lst_graph = []
        i_island = 0
        for i_1 in range(i_h):
            lst_graph.append(list(map(int, sys.stdin.readline().split())))
        for i_2 in range(i_h):
            for i_3 in range(i_w):
                if lst_graph[i_2][i_3] == 1:
                    i_island += 1
                    island_checker(lst_graph, i_3, i_2)
        print(i_island)