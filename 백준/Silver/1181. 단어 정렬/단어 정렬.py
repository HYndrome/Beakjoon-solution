import heapq
import sys

lst_word = []
i_n = int(sys.stdin.readline())
for i_1 in range(i_n):
    s_n = sys.stdin.readline().rstrip()
    lst_word.append(s_n)
lst_word = list(set(lst_word))

heap_word = []
for s_1 in lst_word:
    heapq.heappush(heap_word, (len(s_1), s_1))
for i_1 in range(len(heap_word)):
    print(heapq.heappop(heap_word)[1])