lst_remainder = []
for i_1 in range(10):
    i_n = int(input())
    lst_remainder.append(i_n % 42)
print(len(set(lst_remainder)))