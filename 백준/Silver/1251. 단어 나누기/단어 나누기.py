s_word  = input()
lst_word = []
for i_1 in range(len(s_word) - 2):
    for i_2 in range(i_1 + 1, len(s_word) - 1):
        s_newword = s_word[i_1::-1] + s_word[i_2:i_1:-1] + s_word[-1:i_2:-1]
        lst_word.append(s_newword)
        # print(s_newword)
        # print(s_word[i_1::-1], s_word[i_2:i_1:-1], s_word[:i_2:-1])
print(sorted(lst_word)[0])