i_n, i_k = map(int, input().split())
i_output = 1
for i_1 in range(i_n):
    i_output *= i_1 + 1
for i_2 in range(i_k):
    i_output /= i_2 + 1
for i_3 in range(i_n - i_k):
    i_output /= i_3 + 1
print(int(i_output))    