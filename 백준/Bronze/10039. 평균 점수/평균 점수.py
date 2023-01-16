i_sum = 0
for i_1 in range(5):
    i_input = int(input())
    if i_input < 40:
        i_sum += 40
    else:
        i_sum += i_input
print(int(i_sum/5))