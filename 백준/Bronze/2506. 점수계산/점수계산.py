i_n = int(input())
lst_status = list(map(int, input().split()))
lst_score = []
i_score = 0
for i_1 in lst_status:
    if i_1:
        i_score += 1
    else:
        i_score = 0
    lst_score.append(i_score)
print(sum(lst_score))