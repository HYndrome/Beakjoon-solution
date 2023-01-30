s_a, s_b = input().split()
i_a = int(s_a)
i_b = int(s_b)
i_sum_a = 0
i_sum_b = 0
for i_1 in range(len(s_a)):
    i_a_1 = i_a % 10
    i_a = i_a // 10
    i_sum_a += i_a_1
for i_2 in range(len(s_b)):
    i_b_1 = i_b % 10
    i_b= i_b // 10
    i_sum_b += i_b_1
print(i_sum_a * i_sum_b)