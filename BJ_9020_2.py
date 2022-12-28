import sys

lst_n1 = [i_1 for i_1 in range(10000)]
lst_n1[1] = 0
for i_2 in lst_n1:
    if i_2 == 0:
        continue
    else:
        for i_3 in range(i_2*2, 10000, i_2):
            lst_n1[i_3] = 0
lst_prime = [i_4 for i_4 in lst_n1 if i_4 != 0]

i_t = int(sys.stdin.readline())

for i_t1 in range(i_t):
    i_n = int(sys.stdin.readline())
    lst_prime_n = [i_5 for i_5 in lst_prime if i_5 < i_n]
    lst_goldbach = [i_6 for i_6 in lst_prime_n if lst_n1[i_n - i_6] != 0]
    if len(lst_goldbach)%2 == 1:
        num_m = int((len(lst_goldbach) - 1) / 2) 
        print(lst_goldbach[num_m], lst_goldbach[num_m])
    else:
        num_m1 = int(len(lst_goldbach) / 2 - 1)
        print(lst_goldbach[num_m1], lst_goldbach[num_m1 + 1])