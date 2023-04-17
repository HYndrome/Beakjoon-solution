import sys
# def fibonacci(number):
#     if number == 0:
#         print(0)
#         return 0
#     elif number == 1:
#         print(1)
#         return 1
#     else:
#         return fibonacci(number-1) + fibonacci(number-2)

ls_fibonacci_0 = [0] * 41
ls_fibonacci_1 = [0] * 41

ls_fibonacci_0[0] = 1
ls_fibonacci_1[1] = 1

def bi_fibonacci_0(number):
    if number == 0:
        return ls_fibonacci_0[0]
    elif number == 1:
        return ls_fibonacci_0[1]
    else:
        if ls_fibonacci_0[number - 1] != 0 and ls_fibonacci_0[number - 2] != 0:
            ls_fibonacci_0[number] = ls_fibonacci_0[number - 1] + ls_fibonacci_0[number - 2]
            
        else:
            ls_fibonacci_0[number] = bi_fibonacci_0(number-1) + bi_fibonacci_0(number-2)
    return ls_fibonacci_0[number]

def bi_fibonacci_1(number):
    if number == 0:
        return ls_fibonacci_1[0]
    elif number == 1:
        return ls_fibonacci_1[1]
    else:
        if ls_fibonacci_1[number - 1] != 0 and ls_fibonacci_1[number - 2] != 0:
            ls_fibonacci_1[number] = ls_fibonacci_1[number - 1] + ls_fibonacci_1[number - 2]
            
        else:
            ls_fibonacci_1[number] = bi_fibonacci_1(number-1) + bi_fibonacci_1(number-2)
    return ls_fibonacci_1[number]

i_t = int(sys.stdin.readline())

for i in range(i_t):
    i_n = int(sys.stdin.readline())
    print(bi_fibonacci_0(i_n), bi_fibonacci_1(i_n))
