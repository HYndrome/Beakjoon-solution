import sys
i_n, i_m = map(int, sys.stdin.readline().split())
lst_card = list(map(int, sys.stdin.readline().split()))

i_gap = 300000
lst_print = []
for i_1 in range(len(lst_card) - 2):
    i_sum = lst_card[i_1]
    lst_card_2 = lst_card[i_1 + 1:]
    for i_2 in range(len(lst_card_2)):
        i_sum_2 = i_sum + lst_card_2[i_2]
        lst_card_3 = lst_card_2[i_2 + 1:]
        for i_3 in range(len(lst_card_3)):
            i_sum_3 = i_sum_2 + lst_card_3[i_3]
            i_gap_2 = i_m - i_sum_3
            if i_gap_2 == 0:
                i_gap = i_gap_2
                break
            elif (i_gap_2 > 0) * (i_gap_2 < i_gap):
                i_gap = i_gap_2
print(i_m - i_gap)