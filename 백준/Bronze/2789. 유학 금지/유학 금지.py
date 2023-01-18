s_input = input()
s_ban = 'CAMBRIDGE'
s_output = ''
for s_1 in s_input:
    if s_1 not in s_ban:
        s_output += s_1
print(s_output)