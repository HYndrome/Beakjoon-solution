i_n = int(input())
dict_attendance = {}
for i_1 in range(i_n):
    s_name, s_status = input().split()
    dict_attendance[s_name] = s_status
lst_attendance = []
for key_1, value_1 in dict_attendance.items():
    if value_1 == 'enter':
        lst_attendance.append(key_1)
lst_attendance.sort(reverse= True)
print(*lst_attendance, sep='\n')