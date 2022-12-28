import sys
lst=[]
for i  in range(9):
    a = int(sys.stdin.readline())
    lst.append(a)
for j in range(9):
    if lst[j] == max(lst):
        print(lst[j])
        print(j+1)