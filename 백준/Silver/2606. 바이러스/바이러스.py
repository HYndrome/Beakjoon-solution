import sys

i_n = int(sys.stdin.readline())
lst_graph = [[] for i_1 in range(i_n + 1)]
for i_2 in range(int(sys.stdin.readline())):
    i_comp1, i_comp2 = map(int, sys.stdin.readline().split())
    lst_graph[i_comp1].append(i_comp2)
    lst_graph[i_comp2].append(i_comp1)

lst_connection = [False] * len(lst_graph)

def virus(graph, start, visited):
    visited[start] = True
    for i_3 in graph[start]:
        if not visited[i_3]:
            virus(graph, i_3, visited)
# print(lst_graph)
virus(lst_graph, 1, lst_connection)
# print(lst_connection)
print(sum(lst_connection) - 1)