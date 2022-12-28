current_list = list(map(int,input().split()))
master_list = [1, 1, 2, 2, 2, 8]
gap_list = [current_list[i] - master_list[i] for i in range(len(current_list))]
for i in range(len(current_list)):
    print(gap_list[i],end=" ")