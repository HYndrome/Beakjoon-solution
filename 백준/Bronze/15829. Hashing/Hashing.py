i_l = int(input())
s_input = input()
i_hashing = 0
for i_1 in range(len(s_input)):
    i_hashing += (ord(s_input[i_1]) - 96) * (31 ** i_1)
print(i_hashing % 1234567891)