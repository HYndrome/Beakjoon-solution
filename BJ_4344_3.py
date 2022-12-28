import sys
a = int(sys.stdin.readline())
for i in range(a):
    n, *score_lst = list(map(int, sys.stdin.readline().split()))
    mean = sum(score_lst)/len(score_lst)
    above_lst = []
    for j in score_lst:
        if j > mean:
            above_lst.append(1)
        else:
            above_lst.append(0)
    print(f"{sum(above_lst)/len(above_lst)*100:.3f}%")