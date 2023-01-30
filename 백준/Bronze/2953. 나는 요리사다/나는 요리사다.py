lst_score = [list(map(int, input().split())) for i_1 in range(5)]
i_winner = 1
i_winner_sum = sum(lst_score[0])
for i_2 in range(len(lst_score)):
    if sum(lst_score[i_2]) > i_winner_sum:
        i_winner = i_2 + 1
        i_winner_sum = sum(lst_score[i_2])
print(i_winner, i_winner_sum)