current_list = list(map(int,input().split()))
master_list = [1, 1, 2, 2, 2, 8]
gap_list = [master_list[i] - current_list[i] for i in range(len(current_list))]
print(*gap_list)