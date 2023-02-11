from collections import deque

i_n, i_k = map(int, input().split())
dq_circle = deque([i_1 + 1 for i_1 in range(i_n)])
ls_output = []
while dq_circle:
    dq_circle.rotate(-i_k + 1)
    ls_output.append(dq_circle.popleft())
print('<', end= '')
for i_2 in range(len(ls_output)):
    print(ls_output[i_2], end= '')
    if i_2 != len(ls_output) - 1:
        print(', ', end= '')
print('>')