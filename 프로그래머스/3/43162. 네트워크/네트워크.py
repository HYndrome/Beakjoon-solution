import sys
sys.setrecursionlimit(1000000)
def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    def dfs(i):
        if visited[i] == False:
            visited[i] = True
            index = -1
            for vertex in computers[i]:
                index += 1
                if vertex:
                    dfs(index)
    
    def networkcheck(i):
        nonlocal cnt
        if visited[i] == False:
            cnt += 1
            dfs(i)
    
    for i in range(n):
        networkcheck(i)
    return cnt