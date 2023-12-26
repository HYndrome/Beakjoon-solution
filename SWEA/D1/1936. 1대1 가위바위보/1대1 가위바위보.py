i_a, i_b = map(int, input().split())

if (i_a - i_b == -1) or (i_a - i_b == 2):
    print("B")
elif (i_a - i_b == 1) or (i_a - i_b == -2):
    print("A")