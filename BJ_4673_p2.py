def selfnum(a):
    a_str = str(a)
    for i in range(len(a_str)):
        a += int(a_str[i])
    return a

def findselfnum(b):
    lst_gen=[]
    for i in range(b - 9*len(str(b)),b-1,1):
        if selfnum(i) == b:
            lst_gen.append(i)
    return lst_gen

n = int(input())
while any(lst_gen) <= 2:
    n = findselfnum(n)
a = findselfnum(n)
print(a)