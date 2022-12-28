import sys
a = int(sys.stdin.readline())
for i in range(a):
    score_lst = list(map(int, sys.stdin.readline().split()))
    del score_lst[0] # 제일 왼쪽의 숫자를 처리를 못해서 일단 지워버렸음
    mean = sum(score_lst)/len(score_lst)
    above_lst = []
    for j in score_lst:
        if j > mean:
            above_lst.append(1)
        else:
            above_lst.append(0)
    print(f"{sum(above_lst)/len(above_lst)*100:.3f}%")