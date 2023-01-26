dict_angle = {}
for i_1 in range(3):
    i_angle = int(input())
    dict_angle[i_angle] = dict_angle.get(i_angle, 0) + 1

if sum([key_1 * value_1 for key_1, value_1 in dict_angle.items()]) != 180:
    print('Error')
else:
    if max(dict_angle.values()) == 3:
        print('Equilateral')
    elif max(dict_angle.values()) == 2:
        print('Isosceles')
    else:
        print('Scalene')