def star_append(n):
    if n == 1:
        return ['*']
    comp_star = star_append(n//3)
    lst_star = []
    for s_1 in comp_star:
        lst_star.append(s_1*3)
    for s_2 in comp_star:
        lst_star.append(s_2 + ' '*(n//3) + s_2)
    for s_3 in comp_star:
        lst_star.append(s_3*3)
    return lst_star

i_n = int(input())
print('\n'.join(star_append(i_n)))