# 최대힙
import heapq, sys

i_n = int(sys.stdin.readline())
ls_heap = []
for cal in range(i_n):
    i_x = int(sys.stdin.readline())
    if i_x > 0:
        # 최대힙 입력 부호 반대로 
        heapq.heappush(ls_heap, - i_x)
    elif i_x == 0:
        if ls_heap:
            # 입력을 부호를 반대로 했기 때문에 출력할 때도 반대로 출력
            x_max = - heapq.heappop(ls_heap)
            print(x_max)
        else:
            print(0)