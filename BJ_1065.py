def com_num(a):
    a = int(a)
    if a <= 99:
        return a
    else:
        b = 99
        for i in range(100,a+1):
            a_str = str(i)
            point = 0
            for j in range(0, len(a_str)-2):
                if int(a_str[j+1])*2 == int(a_str[j]) + int(a_str[j+2]):
                    point += 1
            if point == len(a_str)-2:
                b += 1
        return b
n = input()
print(com_num(n))