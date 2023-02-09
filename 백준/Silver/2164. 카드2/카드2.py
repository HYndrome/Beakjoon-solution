from collections import deque

que_input = deque(range(1,int(input()) + 1))
while len(que_input) > 1:
    que_input.popleft()
    que_input.rotate(-1)
print(que_input.pop())