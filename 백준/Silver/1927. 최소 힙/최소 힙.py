import heapq, sys

ls_x = []
i_n = int(sys.stdin.readline())
for i in range(i_n):
    i_x = int(sys.stdin.readline())
    if i_x == 0:
        if not ls_x:
            print(0)
        else:
            i_min = heapq.heappop(ls_x)
            print(i_min)
    else:
        heapq.heappush(ls_x, i_x)