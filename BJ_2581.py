import sys

i_m = int(sys.stdin.readline())
i_n = int(sys.stdin.readline())
lst_prime =[]

for i_r in range(i_m, i_n+1):
    i_d = 2
    while i_d <= i_r:
        if i_r%i_d == 0:
            break
        else:
            i_d += 1
    if i_d == i_r:
        lst_prime.append(i_d)

if not lst_prime:
    print(-1)
else:
    print(sum(lst_prime), min(lst_prime), sep="\n")