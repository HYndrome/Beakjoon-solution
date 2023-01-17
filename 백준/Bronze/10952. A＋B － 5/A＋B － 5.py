while True:
    i_1, i_2 = map(int, input().split())
    if (i_1 == 0) + (i_2 == 0):
        break
    else:
        print(i_1 + i_2)