def selfnum(a):
    a_str = str(a)
    for i in range(len(a_str)):
        a += int(a_str[i])
    return a
lst_selfnum = []
for i in range(1,10001):
    com_selfnum = i
    while com_selfnum <= 10000:
        com_selfnum = selfnum(com_selfnum)
        lst_selfnum.append(com_selfnum)   
lst = [j for j in range(1,10001)]
result = list(set(lst) - set(lst_selfnum))
result.sort()
for k in range(len(result)):
    print(result[k])