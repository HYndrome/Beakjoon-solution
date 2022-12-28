import sys

i_input = int(sys.stdin.readline())
if i_input == 0:
    print("")
else:
    lst_num = [i_num for i_num in range(i_input+1)]
    lst_num[1] = 0

    for i_1 in lst_num:
        if i_1 == 0:
            continue
        else:
            for i_2 in range(i_1*2, i_input+1, i_1):
                lst_num[i_2] = 0

    lst_prime = [i_3 for i_3 in lst_num if lst_num[i_3] != 0]

    i_4 = 0
    while i_input not in lst_prime:
        if i_input % lst_prime[i_4] == 0:
            i_input /= lst_prime[i_4]
            print(lst_prime[i_4])
        else:
            i_4 += 1
    print(f'{i_input:.0f}')
# 시간 초과
# 모든 수에 대해서 prime number을 구하고 시작하니까 시간이 초과가 되는 것 같음