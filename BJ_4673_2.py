def selfnum(a):
    a_str = str(a)
    for i in range(len(a_str)):
        a += int(a_str[i])
    return a
lst_selfnum = []
for i in range(1,10001):
    lst_selfnum.append(selfnum(i))
lst = [j for j in range(1,10001)]
result = list(set(lst) - set(lst_selfnum))
result.sort()
for k in result:
    print(k)