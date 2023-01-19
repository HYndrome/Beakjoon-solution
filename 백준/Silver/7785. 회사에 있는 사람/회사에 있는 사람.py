lst_input = open(0).read().split()[1:]
lst_name = lst_input[::2]
lst_status = lst_input[1::2]
dict_name_status = {}
dict_name_status.update(zip(lst_name, lst_status))
lst_attendance = [key_1 for key_1, value_1 in dict_name_status.items() if value_1 == 'enter']
print(*sorted(lst_attendance, reverse= True))