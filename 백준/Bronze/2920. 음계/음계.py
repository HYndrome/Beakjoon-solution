ls_sound = list(map(int, input().split()))
if ls_sound == [i_1 for i_1 in range(1,9)]:
    print('ascending')
elif ls_sound == [i_2 for i_2 in range(8,0,-1)]:
    print('descending')
else:
    print('mixed')