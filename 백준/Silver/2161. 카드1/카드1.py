i_card = int(input())
lst_card = [i_1 + 1 for i_1 in range(i_card)]
lst_dis = []
while len(lst_card) != 1:
    lst_dis.append(lst_card[0])
    lst_card.pop(0)
    lst_card.append(lst_card[0])
    lst_card.pop(0)
print(*lst_dis, *lst_card)