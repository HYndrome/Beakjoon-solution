s_input = input()
st_input = set()
for i_1 in range(1, len(s_input) + 1):
    for i_2 in range(len(s_input) +  1 - i_1):
        st_input.add(s_input[i_2:i_2 + i_1])
print((len(st_input)))