t = int(input())
for i in range(t):
    r,s = input().split()
    r= int(r)
    for j in s:
        for k in range(r):
            print(j, end="")
    print()