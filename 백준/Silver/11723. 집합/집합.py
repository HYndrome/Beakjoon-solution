import sys

i_m = int(input())
set_cal = set()  
for i in range(i_m):
    ls_1 = sys.stdin.readline().split()
    if ls_1[0] == 'add':
        set_cal.add(int(ls_1[1]))
    elif ls_1[0] == 'remove':
        # if int(ls_1[1]) in set_cal:
        #     set_cal.remove(int(ls_1[1]))
        set_cal.discard(int(ls_1[1]))
    elif ls_1[0] == 'check':
        if int(ls_1[1]) in set_cal:
            print(1)
        else:
            print(0)
    elif ls_1[0] == 'toggle':
        set_cal.symmetric_difference_update([int(ls_1[1])])
    elif ls_1[0] == 'all':
        set_cal = set(range(1, 21))
    else:
        set_cal.clear()