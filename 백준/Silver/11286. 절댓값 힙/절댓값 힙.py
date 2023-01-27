import heapq
import sys

heap_absolute = []
i_n = int(sys.stdin.readline())
for i_1 in range(i_n):
    i_x = int(sys.stdin.readline())
    if i_x > 0:
        heapq.heappush(heap_absolute, (i_x, i_x))
    elif i_x < 0:
        heapq.heappush(heap_absolute, (-i_x, i_x))
    else:
        if heap_absolute:
            print(heapq.heappop(heap_absolute)[1])
        else:
            print(0)