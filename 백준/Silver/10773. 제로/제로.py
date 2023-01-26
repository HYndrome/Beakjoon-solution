import sys

i_k = int(sys.stdin.readline())
lst_stack = []
for i_1 in range(i_k):
    i_input = int(sys.stdin.readline())
    if i_input == 0:
        try:
            lst_stack.pop()
        except IndexError:
            lst_stack.append(0)     
    else:
        lst_stack.append(i_input)
print(sum(lst_stack))