import sys
from collections import deque

i_t = int(sys.stdin.readline())
for i_1 in range(i_t):
    i_n = int(sys.stdin.readline())
    ls_card = sys.stdin.readline().split()
    que_card = deque(ls_card)
    que_sort = deque()
    que_sort.append(que_card.popleft())
    while que_card:
        card_draw = que_card.popleft()
        if card_draw <= que_sort[0]:
            que_sort.appendleft(card_draw)
        else:
            que_sort.append(card_draw)
    for card in que_sort:
        print(card, end='')
    print()