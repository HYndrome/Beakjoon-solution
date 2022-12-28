current_list = list(map(int,input().split()))
master_list = [1, 1, 2, 2, 2, 8]
gap_list = [a - b for a, b in zip(master_list,current_list)]
print(*gap_list)