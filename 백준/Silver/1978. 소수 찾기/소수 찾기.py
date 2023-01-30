import sys
i_case = int(sys.stdin.readline())
lst_n = list(map(int, sys.stdin.readline().split()))
lst_prime = []
for i in lst_n:
    i_d = 2
    while i_d <= i:
        if i%i_d == 0:
            break
        else:
            i_d += 1
    if i_d == i:
        lst_prime.append(i_d)
print(len(lst_prime))