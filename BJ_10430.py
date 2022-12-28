lst = list(map(int,input().split()))
a = lst[0]
b = lst[1]
c = lst[2]
print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, (a%c)*(b%c)%c, sep="\n")