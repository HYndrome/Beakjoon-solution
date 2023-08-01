# 음의 간선, 모든 점의 최단 경로 -> 플로이드 와셜
import sys

INF = int(1e9)
i_tc = int(sys.stdin.readline())
for test_case in range(i_tc):
    i_n, i_m, i_w = map(int, sys.stdin.readline().split())
    graph = [[INF] * (i_n + 1) for _ in range(i_n + 1)]
    # 플로이드와셜 그래프 입력
    # 양방향 도로 입력
    for road in range(i_m):
        start, end, time = map(int, sys.stdin.readline().split())
        if time < graph[start][end]:
            graph[start][end] = time
        if time < graph[end][start]:
            graph[end][start] = time
    # 단방향 웜홀 입력
    for worm_hole in range(i_w):
        start, end, time = map(int, sys.stdin.readline().split())
        if - time < graph[start][end]:
            graph[start][end] = - time
    # 플로이드 와셜 적용 / 시작점 초기화 x
    # 중간에 start end가 같은 지점에서 0보다 작은 경우가 발생 시, 종료
    is_looped = False
    for k in range(1, i_n + 1):
        for start in range(1, i_n + 1):
            for end in range(1, i_n + 1):
                graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])
                if start == end and graph[start][end] < 0:
                    print("YES")
                    is_looped = True
                    break
            if is_looped:
                break
        if is_looped:
            break
    else:
        print("NO")