import sys
while True:
    i_n = int(sys.stdin.readline())
    if i_n != 0:
        lst_n = [i_1 for i_1 in range(2*i_n+1)]
        lst_n[1] = 0
        for i_2 in lst_n:
            if i_2 == 0:
                continue
            else:
                for i_3 in range(i_2*2, 2*i_n + 1, i_2):
                    lst_n[i_3] = 0
        lst_prime = [i_4 for i_4 in range(i_n+1, 2*i_n+1) if lst_n[i_4] != 0]
        print(len(lst_prime))
    else:
        break