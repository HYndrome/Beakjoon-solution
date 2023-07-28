# B가 너무 큰 수라서 제곱으로 나타냄
# A=5 B= 34 C=7 의 경우,
# 5^(2^5) * 5^2 그리고 각 제곱 이후 %7 로 연산 횟수 및 수의 크기를 줄일 수 있음
i_a, i_b, i_c = map(int, input().split())
# print(bi_b)
i_a %= i_c
bi_b = bin(i_b)[2:]
num_current = i_a
num_final = 1
for s in reversed(bi_b):
    if s == "1":
        num_final *= num_current
    num_current **= 2
    num_current %= i_c

num_final %= i_c
print(num_final)