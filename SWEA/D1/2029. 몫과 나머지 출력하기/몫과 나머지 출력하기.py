i_k = int(input())
for i_1 in range(i_k):
    i_a, i_b = map(int, input().split())
    print(f'#{i_1 + 1} {i_a // i_b} {i_a % i_b}')