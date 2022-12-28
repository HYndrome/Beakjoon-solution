v_input = int(input())
num1 = 0
for i in range(1,10000000):
    if num1 >= v_input:
        break
    else:
        num1 += i
if i%2 == 1:
    y = (i-1) - num1 + v_input
    x = 1 + num1 - v_input
else:
    y = 1 + num1 - v_input
    x = (i-1) - num1 + v_input
print(f'{y}/{x}')