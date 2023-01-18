s_s = input()
lst_alphaindex = [-1 for i_1 in range(97, 123)]
for i_1 in range(len(s_s) - 1, -1, -1):
    lst_alphaindex[ord(s_s[i_1]) - 97] = i_1
print(*lst_alphaindex)