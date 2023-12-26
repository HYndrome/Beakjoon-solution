i_n = int(input())
sum_digit = 0
while i_n:
    sum_digit += i_n % 10
    i_n //= 10
print(sum_digit)