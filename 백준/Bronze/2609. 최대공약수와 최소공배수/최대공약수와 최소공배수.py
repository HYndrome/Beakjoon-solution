i_a, i_b = map(int, input().split())
i_gcd = 1
for i_1 in range(1, min(i_a, i_b) + 1):
    if (i_a % i_1 == 0) * (i_b % i_1 == 0):
        i_gcd = i_1
i_lcm = i_a * i_b // i_gcd
print(i_gcd)
print(i_lcm)