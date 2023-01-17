lst_x = []
lst_y = []
for i_1 in range(3):
    i_x, i_y = map(int, input().split())
    lst_x.append(i_x)
    lst_y.append(i_y)
print(min(lst_x, key= lst_x.count), min(lst_y, key= lst_y.count))