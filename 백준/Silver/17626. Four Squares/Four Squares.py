# dp
# 입력
i_n = int(input())
# 제곱수 구하기
current_num = 1
ls_square = []
while True:
    current_num_square = current_num ** 2
    ls_square.append(current_num_square)
    if current_num_square >= i_n:
        break
    current_num += 1
# print(ls_square)
ls_num = [0] * (i_n + 1)
ls_num[1] = 1
for num in range(2, i_n + 1):
    ls_num[num] = min([ls_num[num - square] for square in ls_square if square <= num]) + 1
# print(ls_num)
print(ls_num[i_n])