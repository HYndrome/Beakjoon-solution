i_passenger = 0
lst_passenger = []
for i_1 in range(4):
    i_out, i_in = map(int, input().split())
    i_passenger = i_passenger + i_in - i_out
    lst_passenger.append(i_passenger)
print(max(lst_passenger))