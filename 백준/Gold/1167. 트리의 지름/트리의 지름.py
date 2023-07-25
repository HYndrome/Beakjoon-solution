# 트리의 지름 구하기, dfs
# 문제에서 지나치게 많은 vertex가 있다고 생각했는데, 트리라는 조건이 있었음

# 트리의 지름 구하는 법
# 1. 트리에서 임의의 정점 x 정하기
# 2. 해당 정점 x에서 가장 먼 정점 y찾기
# 3. 정점 y에서 가장 먼 정점 z 찾기
# 4. 트리의 지름 = 정점 y와 정점 z 를 연결하는 경로
import sys

# 재귀 제한 풀기
sys.setrecursionlimit(100000)
# 그래프 입력
# [{이어진 정점: 정점까지의 거리, ...}, ...] 형태로 저장
i_v = int(sys.stdin.readline())
graph = [{}] * (i_v + 1)
for i in range(i_v):
    ls_input = list(map(int, sys.stdin.readline().split()))
    vertex = ls_input[0]
    i = 1
    dct_vertex = {}
    while True:
        if ls_input[i]== -1:
            break
        else:
            dct_vertex[ls_input[i]] = ls_input[i + 1]
            i += 2
    graph[vertex] = dct_vertex

# dfs로 각 정점에서 (다른 정점까지의 최대 거리, 해당 정점)을 return하는 함수
def cal_vertex_d(vertex):
    visited = [0] * (i_v + 1)
    max_d = 0
    sum_d = 0
    max_vertex = 0
    def dfs(v):
        nonlocal max_d, sum_d, max_vertex
        visited[v] = 1
        for nv in graph[v]:
            if visited[nv] == 0:
                sum_d += graph[v][nv]
                if sum_d > max_d:
                    max_d = sum_d
                    max_vertex = nv
                dfs(nv)
                # 되돌아갈경우 더한만큼 빼줌
                sum_d -= graph[v][nv]
    dfs(vertex)
    return max_d, max_vertex

# 트리 지름 구하기
# 1. 트리에서 임의의 정점 x 정하기
# 2. 해당 정점 x에서 가장 먼 정점 y찾기
# 3. 정점 y에서 가장 먼 정점 z 찾기
# 4. 트리의 지름 = 정점 y와 정점 z 를 연결하는 경로
# 트리 지름 계산 = 각 정점의 최대거리 중 최댓값

vertex_x = 1
vertex_y = cal_vertex_d(vertex_x)[1]
tree_diameter = cal_vertex_d(vertex_y)[0]
# 출력
print(tree_diameter)