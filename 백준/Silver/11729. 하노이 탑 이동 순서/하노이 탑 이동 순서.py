i_n = int(input())
lst_hanoi = []

def hanoi(n, p_start, p_end):
    p_neu = [i_1 for i_1 in [1, 2 ,3] if i_1 != p_start and i_1 != p_end][0]
    if n == 1:
        lst_hanoi.append((p_start, p_end))
        return
    hanoi(n-1, p_start, p_neu)
    hanoi(1, p_start, p_end)
    hanoi(n-1, p_neu, p_end)
    return

hanoi(i_n, 1, 3)
print(len(lst_hanoi))
for tup_1 in lst_hanoi:
    print(*tup_1)