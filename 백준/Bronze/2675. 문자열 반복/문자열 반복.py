i_t = int(input())
for i_1 in range(i_t):
    s_r, s_word = input().split()
    s_output = ''
    for s_1 in s_word:
        s_output += int(s_r) * s_1
    print(s_output)