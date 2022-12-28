a = input()
c_1 = a.count('c=')
c_2 = a.count('c-')
c_3 = a.count('dz=')
c_4 = a.count('d-')
c_5 = a.count('lj')
c_6 = a.count('nj')
c_7 = a.count('s=')
c_8 = a.count('z=')
count_total = len(a) - c_1 - c_2 - c_3 - \
    c_4 - c_5 - c_6 - c_7 - c_8
print(count_total)