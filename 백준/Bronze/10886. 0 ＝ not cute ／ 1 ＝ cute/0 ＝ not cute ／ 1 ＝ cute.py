i_n = int(input())
i_sum = 0
for i_1 in range(i_n):
    i_cute = int(input())
    i_sum += i_cute
if i_sum >= (i_n + 1) / 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")