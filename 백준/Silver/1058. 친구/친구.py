import sys


i_n = int(sys.stdin.readline())
graph = [sys.stdin.readline().rstrip() for _ in range(i_n)]

i_popular = 0
for y in range(i_n):
    set_y = set()
    for x in range(i_n):
        if graph[y][x] == 'Y':
            set_y.add(x)
            for k in range(i_n):
                if (graph[x][k] == 'Y') and (y != k):
                    set_y.add(k)
    i_cnt = len(set_y)
    if i_cnt > i_popular:
        i_popular = i_cnt
        
print(i_popular)