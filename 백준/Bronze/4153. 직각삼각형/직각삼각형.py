while True:
    lst_tri = sorted(list(map(int, input().split())))
    if sum(lst_tri) == 0:
        break
    else:
        if (lst_tri[0])**2 + (lst_tri[1])**2 - (lst_tri[2])**2 == 0:
            print('right')
        else:
            print('wrong')