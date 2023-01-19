i_mult = 1
for i_1 in range(3):
    i_n = int(input())
    i_mult *= i_n
lst_digit = [0 for i_2 in range(10)]
for s_1 in str(i_mult):
    lst_digit[int(s_1)] += 1
print(*lst_digit, sep= '\n')